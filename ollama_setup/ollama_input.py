import json
import os
import urllib.error
import urllib.parse
import urllib.request

LOCAL_OLLAMA_HOST = "127.0.0.1"
LOCAL_OLLAMA_PORT = 11435
MODEL_NAME = "gpt4o-mini"
OUTPUT_FILE = "ollama_response.txt"


def call_local_ollama(prompt, model, host, port):
    url = f"http://{host}:{port}/api/generate"
    english_prompt = f"Answer in English only.\n\n{prompt}"
    body = json.dumps({"model": model, "prompt": english_prompt, "stream": False}).encode("utf-8")
    headers = {"Content-Type": "application/json"}
    
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            raw = response.read()
            if not raw:
                raise RuntimeError("Empty response from Ollama")
            data = json.loads(raw.decode("utf-8"))
            text = data.get("response", "")
            if text:
                return text.strip()
            raise RuntimeError(f"No response text in Ollama reply: {data}")
    except urllib.error.HTTPError as exc:
        try:
            error_body = exc.read().decode("utf-8")
        except Exception:
            error_body = ""
        print(f"HTTP error from Ollama ({url}): {exc.code} {exc.reason}")
        if error_body:
            print("Response body:", error_body)
        raise
    except urllib.error.URLError as exc:
        print(f"Unable to connect to Ollama at {url}: {exc}")
        print(f"Make sure Ollama is running at http://{host}:{port}")
        raise
    except json.JSONDecodeError as exc:
        print(f"Invalid JSON response from Ollama at {url}: {exc}")
        raise


def write_response_to_file(text, filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    user_input = input("Enter a prompt for Ollama: ").strip()
    if not user_input:
        print("No prompt entered. Exiting.")
        raise SystemExit(1)

    model = os.environ.get("OLLAMA_MODEL", MODEL_NAME)
    host = os.environ.get("OLLAMA_HOST", LOCAL_OLLAMA_HOST)
    port = int(os.environ.get("OLLAMA_PORT", LOCAL_OLLAMA_PORT))

    print(f"Sending prompt to local Ollama model '{model}' at {host}:{port}...")
    response_text = call_local_ollama(user_input, model, host, port)
    write_response_to_file(response_text, OUTPUT_FILE)
    print(f"Response written to {OUTPUT_FILE}")
