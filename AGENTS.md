# AGENTS.md

## Project Objective

This repository contains the 2026 edition of the 90 Days of DevOps challenge. The usual task is to complete one specific day by reading its `README.md`, performing the practical work, and documenting the result.

## Default Interpretation

When the user says `day X`, `advance to day X`, or equivalent:

1. Work only in `2026/day-X/`.
2. Read that day's `README.md` completely before changing files.
3. Inspect only files required to understand and complete that day.
4. Treat the README's challenge tasks, expected output, documentation, and submission sections as the specification.
5. Implement and validate the exercises; do not stop at a plan unless the user explicitly asks for one.

Never modify another day, files outside `2026`, or repository-wide configuration unless the user explicitly requests it. The only exception is this root `AGENTS.md` itself.

## Scope and Change Discipline

- Keep changes small, local, and easy to review.
- Work only inside the requested day's directory.
- Do not refactor, reorganize, or reformat unrelated files.
- Do not invent commands, exercises, dependencies, or artifacts not supported by the day's content.
- Preserve useful existing content and avoid duplication.
- Do not modify the day's `README.md` unless explicitly requested.
- Never revert pre-existing or unrelated changes.

## Required Day Files

- Always create or update `notes.md` with a short, factual summary.
- Create or update `tasks.md` only when the day has clear commands or practical tasks.
- In `tasks.md`, document every command and explain what it does, preferably in a `Command | What it does` table.
- Create the documentation file named in the README's expected output.
- Create required source files, manifests, Dockerfiles, Compose files, scripts, workflows, or configs inside that day's directory.
- Use a simple structure; add subdirectories only when useful or required.
- Do not create screenshots. Record relevant output as concise text unless screenshots are explicitly requested.

All created or updated challenge content must be in English, including Markdown, comments, sample output, and commit messages.

## Implementation Workflow

1. Inspect the requested day's README and existing files.
2. Check Git status for that directory.
3. Identify exact deliverables and practical validation steps.
4. Reuse relevant patterns established by previous days.
5. Create or update the smallest necessary set of files.
6. Validate syntax before applying or running resources.
7. Execute the exercise when the local environment supports it.
8. Record only factual results; never fabricate successful output.
9. Clean up temporary files and resources when requested.
10. Run final scope, language, syntax, and whitespace checks.

## Validation Rules

- Prefer real execution over assumed results.
- Use the appropriate existing validation: tests, lint, build, Docker, Docker Compose, `kubectl`, or GitHub CLI.
- For Kubernetes, validate client-side first and use server-side dry-run when a cluster is available.
- For Docker, verify builds and runtime behavior when Docker is available.
- For GitHub Actions, validate YAML locally where practical and inspect runs with `gh` when access is available.
- Do not install dependencies unless required; explain the reason first.
- Prefer user-local installation over `sudo`.
- Never say a command passed unless it actually ran successfully.
- If validation is unavailable, state the exact limitation and preserve the intended commands in `tasks.md`.

## Commands in tasks.md

- Assume commands run from the day's directory unless stated otherwise.
- Explain important flags.
- Distinguish alternatives from commands that must all run.
- Warn when a command deletes resources, overwrites state, publishes an image, opens a pull request, or pushes commits.
- Exclude one-off diagnostics unless useful for repeating or troubleshooting the exercise.
- Include cleanup commands for temporary containers, Pods, clusters, services, and similar resources.

## Git Conventions

Do not commit, push, open pull requests, or create branches unless explicitly requested or required by the day's exercise. Documentation may show those commands without executing them.

- `AFarinha/github-actions-practice` uses `main`.
- `AFarinha/90DaysOfDevOps` uses `master`.
- When `github-actions-practice` is nested in a day, commit and push it first. Then commit the nested repository reference and day documentation in the parent repository.
- Do not create a branch unless the day's task explicitly requires one, such as a pull request exercise.
- Commit messages use: `Day X - Completed - <English description>`.
- If a pull request is required, create and document it rather than bypassing the exercise with a direct commit.
- Never commit local environments, caches, runner installations, credentials, build output, or downloaded archives. Examples: `.venv/`, `__pycache__/`, `actions-runner/`, `.env`, and tool binaries.

## Security

- Never put tokens, passwords, Docker credentials, kubeconfig contents, private keys, or secrets in committed files or copied command output.
- Use placeholders and environment-variable names in examples.
- Keep `.env` local; add `env.sample` only when configuration is required.
- Check generated workflows and configs for accidental secret exposure.

## Documentation Quality

- Explain concepts directly and practically.
- Keep `notes.md` concise; use the named day document for the full report.
- Include versions and results only when verified.
- Explain relevant failures and lessons.
- Avoid duplicating full sections across `notes.md`, `tasks.md`, and the main document.
- Use ASCII by default and preserve existing Markdown style.

## Completion Checklist

Confirm that:

- every requested deliverable is inside `2026/day-X/`;
- all new challenge content is in English;
- every command in `tasks.md` has an explanation;
- no temporary, secret, cache, binary, screenshot, or unrelated file was added;
- practical validation ran where possible;
- requested cleanup was completed;
- no task-created changes exist outside the requested day;
- no commit or push occurred without authorization.

## Final Response

Respond in European Portuguese unless requested otherwise. Briefly report:

- the day processed;
- files created or updated;
- practical exercises and validation results;
- cleanup state;
- limitations or assumptions;
- whether commit and push were performed.
