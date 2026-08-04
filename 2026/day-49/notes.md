# Day 49 Notes - DevSecOps

## Summary

DevSecOps integrates security checks into the same CI/CD flow used to build, test, and deploy an application. The Day 48 pipeline now reviews dependency changes in pull requests, scans the locally built Docker image before publishing it, and limits workflow token permissions.

## Implemented Security Controls

- The PR pipeline uses actions/dependency-review-action@v5 and fails when a pull request introduces a dependency with a critical vulnerability.
- The reusable Docker workflow builds the image locally, scans vulnerabilities with aquasecurity/trivy-action@v0.36.0 and Trivy v0.73.0, and only logs in and pushes after the scan succeeds.
- The main, PR, and reusable Docker workflows use contents: read permissions.
- Trivy checks operating-system and application-library vulnerabilities with CRITICAL or HIGH severity.
- The Docker base image being scanned is python:3.12-slim.

## Secure Pipeline

~~~text
Pull request
  -> build and test
  -> review changed dependencies
  -> pass or block the pull request

Merge to main
  -> build and test
  -> build Docker image locally
  -> scan image with Trivy
  -> log in to Docker Hub
  -> push approved image tags
  -> deploy

Always active on GitHub
  -> secret scanning detects committed credentials
  -> push protection blocks supported secrets before they are pushed
~~~

## Secret Scanning and Push Protection

Secret scanning examines repository content and creates an alert when it detects a supported credential pattern. Push protection runs earlier and blocks a push that contains a supported secret before it reaches the repository.

If an AWS key is detected after it was committed, revoke or rotate it immediately, remove it from the code and Git history when necessary, and replace it with a GitHub Secret. If push protection detects it first, the push is blocked and the key must be removed before retrying.

## Least Privilege

Limiting the workflow token to contents: read reduces the impact of a compromised third-party action. An action with unnecessary write access could modify repository content, releases, pull requests, or other resources available to its token.

## Scan Results

GitHub Actions run 30914659198 scanned the image built from python:3.12-slim and produced the following result:

- Target: github-actions-practice:latest on Debian 13.6.
- Operating-system packages: 23 findings, including 19 HIGH and 4 CRITICAL.
- Python packages: 0 vulnerabilities.
- Fixed Version was empty for the reported Debian findings.

The distinct CVEs shown in the report were:

- util-linux package family: CVE-2026-53615.
- gzip: CVE-2026-41992.
- libacl1: CVE-2026-54369.
- ncurses package family: CVE-2025-69720.
- perl-base: CVE-2026-13221, CVE-2026-42496, CVE-2026-57433, CVE-2026-8376, CVE-2026-42497, CVE-2026-48962, CVE-2026-57432, and CVE-2026-9538.

The scan correctly returned exit code 1. Docker Hub login, image push, and production deployment were skipped.

Screenshots are intentionally not included.
