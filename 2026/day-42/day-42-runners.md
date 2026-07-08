# Day 42 Runners

## GitHub-Hosted Runner

A GitHub-hosted runner is a temporary virtual machine managed by GitHub. GitHub provisions it for the job, includes a set of pre-installed tools, runs the job, and then discards the environment.

This is useful because every job starts from a clean environment without needing to maintain your own runner machine.

## Pre-installed Tools

GitHub-hosted runners include many common tools such as Git, Python, Node.js and Docker on Linux runners. This matters because pipeline jobs can start faster and need less setup code.

Always check the current runner image documentation when a pipeline depends on a specific tool version.

## Self-Hosted Runner

A self-hosted runner is a machine you manage and register with GitHub Actions. It can be your local machine, a VM, a cloud instance or an internal server.

Screenshots to add after setup:

```text
Self-hosted runner idle screenshot: <add-screenshot>
Self-hosted job run screenshot: <add-screenshot>
```

## Self-Hosted Workflow

The workflow in `github-actions-practice/.github/workflows/self-hosted.yml` targets:

```yaml
runs-on:
  - self-hosted
  - linux
  - my-linux-runner
```

This means the job will only run on a self-hosted runner that has all three labels.

## Why Labels Matter

Labels are useful when you have multiple self-hosted runners. They let you route jobs to the right machine based on operating system, installed tools, network access or hardware.

Examples:

- `linux`
- `gpu`
- `staging-network`
- `my-linux-runner`

## GitHub-Hosted vs Self-Hosted

| | GitHub-Hosted | Self-Hosted |
|---|---|---|
| Who manages it? | GitHub manages provisioning, patching and cleanup. | You manage the machine, updates, security and availability. |
| Cost | Included by GitHub Actions minutes and plan limits. | You pay for your own machine, VM or infrastructure. |
| Pre-installed tools | Many common tools are already installed. | You decide what is installed. |
| Good for | General CI jobs, open-source projects and clean repeatable builds. | Private networks, custom tools, special hardware or long-running internal workloads. |
| Security concern | Less control over the environment, but it is ephemeral. | More control, but secrets and workspace files can remain on your machine if not cleaned carefully. |

## What I Learned

- Every job needs a runner.
- `runs-on` selects the runner type or labels.
- GitHub-hosted runners are easier to use.
- Self-hosted runners are more flexible but require maintenance.

