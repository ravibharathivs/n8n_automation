# AI Resume Creator

## Naukri Job Scraper via Apify

To use the Naukri job scraper from Apify, follow these steps:

1. Open the Apify website at https://apify.com.
2. Create an account or sign in if you already have one.
3. In the Apify dashboard, go to "Actors" and search for a Naukri scraper. A common actor name is "Naukri job scraper" or similar.
4. Open the actor page and check the available input fields and instructions.
5. To call the actor via API, you need your Apify API token.

### Get Apify API Token

1. Click your profile icon in the top-right corner and select "Account settings".
2. Navigate to the "API tokens" section.
3. Create a new API token or copy an existing one.
4. Keep the token secret.

### Example API Request

Use the Apify API endpoint to run the actor and get results.

- Endpoint: `https://api.apify.com/v2/acts/{username}~{actor-name}/runs?token={APIFY_TOKEN}`
- Replace `{username}` and `{actor-name}` with the actual actor owner and actor slug.
- Replace `{APIFY_TOKEN}` with your API token.

Example using `curl`:

```bash
curl \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "startUrls": [
      {"url": "https://www.naukri.com/jobs-data-scientist"}
    ],
    "maxItemsPerCrawl": 50
  }' \
  "https://api.apify.com/v2/acts/username~naukri-job-scraper/runs?token=YOUR_APIFY_TOKEN"
```

### Notes

- The exact actor slug may vary, so verify the name on the Apify actor page.
- The request body depends on the actor's input schema.
- After the actor finishes, you can download results from the run details or use the Apify API to fetch the dataset.
