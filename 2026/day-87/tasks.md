# Day 87 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `mkdir -p .runtime/models; python3 -m venv .venv` | Create ignored model cache and isolated Python environment. |
| `.venv/bin/pip install -r requirements.txt; .venv/bin/pip check` | Install the authorized reference dependencies and check compatibility. |
| `git clone --depth 1 https://github.com/TrainWithShubham/agentic-ai-for-devops.git .runtime/agentic-ai-for-devops` | First run only: obtain reference modules for comparison. |
| `docker run -d --name days87-ollama -p 127.0.0.1:11434:11434 -v "$PWD/.runtime/models:/root/.ollama" ollama/ollama` | Run the local LLM on loopback; image/model downloads use significant disk space. |
| `docker exec days87-ollama ollama pull gemma4; docker exec days87-ollama ollama list` | Obtain and verify the specified local model. |
| `.venv/bin/python .runtime/agentic-ai-for-devops/module-0/verify_setup.py` | Reference preflight; host Ollama check is expected to fail for the containerized alternative. |
| `docker run -d --restart on-failure:5 --name days87-broken nginx:alpine sh -c 'echo app-starting && sleep 2 && exit 1'` | Create the controlled crashing container with an actual bounded restart policy. |
| `.venv/bin/python explainer.py 'Conflict. The container name /myapp is already in use.'` | Execute one model explanation; no fixes are applied. |
| `.venv/bin/python agent.py 'Why is days87-broken crashing?'` | Run the Docker agent and record its selected tools and evidence-based diagnosis. |
| `.venv/bin/python agent.py 'What images do I have and how much space do they use?'` | Exercise the added list_images tool. |
| `docker logs --tail 10 days87-broken; docker inspect --format '{{json .State}}' days87-broken` | Inspect bounded actual failure evidence without environment variables. |
| `docker rm -f days87-broken days87-ollama` | Destructive cleanup of only the named task-created containers; ignored cache/venv remain local. |
