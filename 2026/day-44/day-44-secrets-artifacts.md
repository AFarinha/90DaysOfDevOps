# Day 44 Secrets, Artifacts and Real Tests

## Workflow File

File: `github-actions-practice/.github/workflows/secrets-artifacts-tests.yml`

This workflow demonstrates:

- checking whether a secret is set without exposing its value;
- passing a secret as an environment variable;
- uploading an artifact;
- downloading the artifact in another job;
- caching pip dependencies;
- running real Python tests in CI.

## Secrets

Required repository secrets:

| Secret | Purpose |
|---|---|
| `MY_SECRET_MESSAGE` | Used to verify that secrets are available inside the workflow. |
| `DOCKER_USERNAME` | Prepared for future Docker Hub login workflows. |
| `DOCKER_TOKEN` | Prepared for future Docker Hub login workflows. |

The workflow does not need to print the secret value. It only checks whether it is non-empty:

```bash
if [ -n "$MY_SECRET_MESSAGE" ]; then
  echo "The secret is set: true"
else
  echo "The secret is set: false"
fi
```

If a secret is printed directly, GitHub masks the value in logs as `***`. Even so, secrets should not be printed because masking is a safety net, not a logging strategy.

## Artifacts

The workflow creates a report file:

```text
reports/test-report.txt
```

Then it uploads the report using:

```yaml
uses: actions/upload-artifact@v4
```

A second job downloads it using:

```yaml
uses: actions/download-artifact@v4
```

Artifacts are useful for:

- test reports;
- logs;
- coverage reports;
- binaries;
- build outputs;
- deployment packages.

## Caching

The workflow caches pip dependencies with `actions/cache@v4`.

The cached path is:

```text
~/.cache/pip
```

The cache is stored by GitHub Actions and restored in later workflow runs when the cache key matches.

## Real Tests

The workflow runs:

```bash
python -m pytest -q
```

If a test fails, pytest exits with a non-zero status and the pipeline goes red.

## Screenshots

Add screenshots after running the workflow:

```text
Artifact download screenshot: <add-screenshot>
Passing test run screenshot: <add-screenshot>
```

## What I Learned

- Secrets should be injected at runtime, never hardcoded.
- Artifacts preserve outputs from CI jobs for later inspection or reuse.
- Caching speeds up dependency installation.
- Real tests make CI useful because failed code blocks the pipeline.

