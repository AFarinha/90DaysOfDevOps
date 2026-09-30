# Day 88 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `export KUBECONFIG="$PWD/../day-84/.runtime/kubeconfig"` | Use the dedicated disposable cluster. Commands reuse Day 87's authorized venv. |
| `kubectl create namespace days88-lab` | First run only: isolated namespace. |
| `kubectl apply --dry-run=server -f broken-pod.yaml; kubectl apply -f broken-pod.yaml` | Validate then deploy the intentionally crashing Pod. |
| `docker run -d --restart on-failure:5 --name days88-broken nginx:alpine sh -c 'echo container-starting && sleep 2 && exit 1'` | Optional second Docker failure fixture; keep it separate from Day 87. |
| `../day-87/.venv/bin/python agent.py 'What is broken across Docker and Kubernetes?'` | Run the multi-domain agent with bounded tools. |
| `../day-87/.venv/bin/python mcp_server.py` | Start the MCP stdio server; a client normally launches it as a subprocess. |
| `../day-87/.venv/bin/python validate-mcp.py` | Test real tool discovery and read-only invocations without LLM substitution. |
| `../day-87/.venv/bin/python mcp_client.py 'Why is broken-pod crashing?'` | Run a model-driven diagnosis with tools discovered through MCP. |
| `CI_REPOSITORY=AFarinha/90DaysOfDevOps ../day-87/.venv/bin/python ci_analyzer.py 'What failed in my last CI run?'` | Run from the target checkout when workflow-file reading is needed; requires authenticated gh. |
| `gh run list --repo AFarinha/90DaysOfDevOps --status failure --limit 5 --json databaseId,name,conclusion` | Read-only prerequisite check for real failures; an empty list is not an analyzer success. |
| `kubectl delete namespace days88-lab; docker rm -f days88-broken` | Destructive disposable-fixture cleanup; skip the container deletion if the optional fixture was not created. |
