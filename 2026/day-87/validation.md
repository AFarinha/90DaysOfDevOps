# Day 87 Validation

- Python dependencies installed in the ignored .venv; pip check passed.
- Ollama ran in the loopback-only days87-ollama Docker container.
- gemma4:latest downloaded successfully: model ID dc35e8d9c606, size 6.6GB as reported by ollama list.
- The reference preflight was executed with a documented local wrapper delegating ollama to docker exec; result recorded below after final checks.
- days87-broken deliberately printed app-starting and exited 1 with on-failure:5.
- Initial explainer and Docker diagnosis timed out (exit 124) on CPU. The clients were changed to reasoning=False/think=False and a 256-token generation bound for a repeat.
- The added list_images tool was selected by the actual model; the process exited 0. Its answer reached the generation limit before listing every image, so completeness is not claimed.

Final repeat results and cleanup are appended after execution.

## Successful repeat
- Reference setup preflight: 5/5 passed using the containerized Ollama wrapper and the verified WSL tool PATH.
- explainer_retry_exit=0: explained that the existing myapp container reserves its name and offered removal/renaming alternatives. No model-suggested cleanup command was executed.
- docker_agent_retry_exit=0: the model selected inspect_container and identified the deliberate sh command's exit 1 after two seconds.
- images_agent_exit=0: the model selected list_images; its long answer was truncated by the generation bound, so a complete inventory is not claimed.
- Model-generated commands are suggestions, not validated remediation.

## Prompt comparison
With the same conflict error and temperature 0.3, a two-bullet inspection-first prompt produced a shorter answer than the default three-part prompt. It also suggested a "stale image" as a possible source of the conflict, which is inaccurate: images do not reserve container names. The experiment shows that format compliance does not establish diagnosis accuracy.

## Final scope and cleanup
The task-created days81-90-lab cluster and days87-broken, days87-ollama and days89-temporal containers were removed successfully. Only the pre-existing devops-cluster remains; its default context is unchanged and its node was verified Ready.

Sources, virtual environments, model cache and private test history remain only in ignored local directories for reproducibility. No AWS resources were created. Final Python/YAML syntax, Terraform formatting, whitespace, credential-pattern and Git scope checks passed; no README or file outside days 81-90 was changed. No commit, push or social post was performed.
