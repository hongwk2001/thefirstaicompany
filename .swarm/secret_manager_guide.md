# 🔒 Google Cloud Secret Manager Integration Guide

To satisfy the token/key context boundary constraints, all corporate keys, tokens, and publishing handles should be stored securely in **Google Cloud Secret Manager** rather than local environment files.

## 1. Setup in GCP
Create secrets in your Google Cloud Project:
- `projects/YOUR_PROJECT_ID/secrets/TWITTER_BEARER_TOKEN`
- `projects/YOUR_PROJECT_ID/secrets/GITHUB_TOKEN`

Ensure the service account running your agent/app has the `Secret Manager Secret Accessor` role (`roles/secretmanager.secretAccessor`).

## 2. Programmatic Secret Retrieval (Node.js)

Install the Secret Manager client:
```bash
npm install @google-cloud/secret-manager
```

Use the following helper to retrieve secrets directly at runtime:

```javascript
const { SecretManagerServiceClient } = require('@google-cloud/secret-manager');

const client = new SecretManagerServiceClient();

async function getSecret(secretName, projectId = 'your-gcp-project-id') {
  try {
    const [version] = await client.accessSecretVersion({
      name: `projects/${projectId}/secrets/${secretName}/versions/latest`,
    });
    
    // Extract the secret payload
    const payload = version.payload.data.toString('utf8');
    return payload;
  } catch (error) {
    console.error(`Error retrieving secret ${secretName}:`, error);
    throw error;
  }
}

module.exports = { getSecret };
```

Using this pattern eliminates the risk of local file leaks or committing credentials to git.
