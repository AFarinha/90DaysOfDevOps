# Day 88 Validation

- broken-pod.yaml passed server dry-run and produced real CrashLoopBackOff/Error with repeated exit code 1 in days88-lab.
- MCP stdio discovery returned describe_pod, get_events, list_pods and search_logs.
- Real list_pods invocation returned the failed Pod; describe_pod returned crash evidence; literal search found app starting in broken-pod logs.
- This protocol smoke test uses no LLM and is recorded separately from model-driven tool selection.
- Authenticated GitHub CLI query for the five recent failed runs in AFarinha/90DaysOfDevOps returned an empty JSON array. No failed run or successful failure diagnosis is invented.
- Python/YAML parsing and dependency compatibility checks passed.

Final model-driven agent results and cleanup are appended after execution.

## Model-driven repeat
The first test process omitted the WSL user-local tool directory from PATH. Its MCP model answer correctly reported kubectl unavailable; the first multi-agent result did not provide a complete final diagnosis. After fixing PATH, multi_agent_retry_exit=0 selected inspect_container and describe_pod and explained that both startup commands intentionally exit 1.

The CI analyzer returned: "There are no recent failed workflow runs." This agrees with the independent empty gh query; it is not a demonstrated failure diagnosis.

## MCP and custom tool repeat
- mcp_agent_retry_exit=0: with the corrected WSL PATH, the model used MCP-provided pod details and explained the explicit exit 1 command behind CrashLoopBackOff.
- The model selected search_logs for "app starting" and reported the actual broken-pod match.
- Both protocol-only validation and model-driven diagnosis were completed; no failed GitHub workflow was available for a failure-analysis demonstration.

## Final scope and cleanup
The task-created days81-90-lab cluster and days87-broken, days87-ollama and days89-temporal containers were removed successfully. Only the pre-existing devops-cluster remains; its default context is unchanged and its node was verified Ready.

Sources, virtual environments, model cache and private test history remain only in ignored local directories for reproducibility. No AWS resources were created. Final Python/YAML syntax, Terraform formatting, whitespace, credential-pattern and Git scope checks passed; no README or file outside days 81-90 was changed. No commit, push or social post was performed.
