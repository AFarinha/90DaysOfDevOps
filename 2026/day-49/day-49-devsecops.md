# Day 49 - DevSecOps Security Checks

## What DevSecOps Means

DevSecOps makes security checks part of the normal development and delivery pipeline instead of a separate review performed after deployment. Pull requests and release builds are checked automatically, and serious findings stop the pipeline before vulnerable code or images reach production.

## Implemented Controls

| Pipeline stage | Security control | Failure policy |
| --- | --- | --- |
| Pull request | GitHub dependency review | Fail when a changed dependency introduces a critical vulnerability. |
| Docker build | Trivy image scan | Fail on high or critical operating-system or library vulnerabilities. |
| Docker publication | Registry login and push | Run only after the Trivy scan succeeds. |
| Workflow execution | Least-privilege token | Limit repository content access to read-only. |
| Repository protection | Secret scanning | Alert when GitHub detects a supported committed credential. |
| Push protection | Pre-push secret check | Block supported credentials before they reach the repository. |

## Pipeline Diagram

~~~text
feature/day-49-devsecops
        |
        v
Pull request to main
        |
        +--> reusable build and Python tests
        |
        +--> dependency review
                 |
                 +--> critical finding: block merge
                 |
                 +--> no critical finding: allow review and merge

main
  |
  v
reusable build and Python tests
  |
  v
build local Docker image
  |
  v
Trivy scan: HIGH and CRITICAL
  |
  +--> finding: fail before registry login
  |
  +--> pass: Docker Hub login -> push tags -> deploy
~~~

## Docker Image Scan

The reusable Docker workflow scans the first generated image tag after Buildx loads the image into the runner's local Docker engine:

~~~yaml
- name: Scan Docker image for vulnerabilities
  uses: aquasecurity/trivy-action@v0.36.0
  with:
    image-ref: ${{ steps.image-tags.outputs.image_url }}
    format: table
    exit-code: "1"
    severity: CRITICAL,HIGH
    scanners: vuln
    version: v0.73.0
~~~

The image uses python:3.12-slim as both the builder and runtime base.

GitHub Actions run 30914659198 produced these scan results:

- Debian 13.6 packages: 23 findings, including 19 HIGH and 4 CRITICAL.
- Python packages: 0 vulnerabilities.
- Critical CVEs: CVE-2026-13221, CVE-2026-42496, CVE-2026-57433, and CVE-2026-8376.
- High-severity findings included the util-linux, gzip, libacl1, ncurses, and perl-base package families.

The Fixed Version column was empty for the reported Debian vulnerabilities, with findings marked affected or fix_deferred.

Because the scan returned exit code 1, Docker Hub login, image publication, and deployment were correctly skipped.

## Dependency Review

The PR pipeline uses actions/dependency-review-action@v5. It compares dependency changes introduced by the pull request and fails when the new dependency set contains a critical vulnerability.

~~~yaml
- name: Check dependencies for vulnerabilities
  uses: actions/dependency-review-action@v5
  with:
    fail-on-severity: critical
~~~

## Secret Protection

Secret scanning examines repository content and raises alerts for supported credential patterns. Push protection checks changes earlier and can reject a push before a supported secret is stored in the repository.

When a leaked AWS key is detected, revoke or rotate it immediately. Removing only the visible line is insufficient if the credential remains active or is still present in Git history.

## Workflow Permissions

The main pipeline, PR pipeline, and reusable Docker workflow declare:

~~~yaml
permissions:
  contents: read
~~~

This follows least privilege: the workflows can read the checked-out source but cannot modify repository contents with GITHUB_TOKEN.

## Verification

1. Open the Day 49 pull request and confirm that both the Python tests and dependency review pass.
2. Merge the pull request into main.
3. Open the main pipeline run and inspect the Scan Docker image for vulnerabilities table.
4. Confirm that Docker Hub login, image push, and deployment occur only after a successful scan.
5. Record any reported CVE, affected package, installed version, and fixed version in notes.md.

Screenshots are intentionally not included; the workflow definitions and GitHub Actions logs provide the required code and execution evidence.
