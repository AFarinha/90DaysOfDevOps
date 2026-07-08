# Notes - Day 44

Summary: Use GitHub Actions secrets, artifacts, caching and real tests in CI.

- Secrets should be stored in GitHub Actions secrets, not hardcoded in workflow files.
- GitHub masks secret values in logs, but workflows should avoid printing secrets directly.
- Artifacts store files produced by jobs, such as reports, logs and build outputs.
- Artifacts can be uploaded in one job and downloaded in another job.
- Caching speeds up repeated dependency installation by reusing files between workflow runs.
- Real tests should fail the pipeline when scripts exit with a non-zero status.

