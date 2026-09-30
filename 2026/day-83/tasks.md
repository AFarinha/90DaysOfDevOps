# Day 83 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `export KUBECONFIG="$PWD/../day-81/.runtime/eks-kubeconfig"` | Select the EKS exercise context; local checks use day-84's dedicated kubeconfig. |
| `kubectl wait --for=condition=ready pod -l app=mysql -n bankapp --timeout=120s` | Wait for database readiness after Day 81 deployment. |
| `kubectl wait --for=condition=ready pod -l app=ollama -n bankapp --timeout=600s; kubectl wait --for=condition=ready pod -l app=bankapp -n bankapp --timeout=300s` | Wait for AI model service and app startup. |
| `kubectl create namespace monitoring` | First run only: create the monitoring namespace. |
| `python3 create-monitoring-secret.py` | Generate a private Grafana credential Secret without recording passwords. |
| `helm template monitoring kube-prometheus-stack --repo https://prometheus-community.github.io/helm-charts --version 65.8.1 -n monitoring -f monitoring-values.yaml` | Render the selected chart before deployment; existingSecret keeps credentials outside values. |
| `helm upgrade --install monitoring kube-prometheus-stack --repo https://prometheus-community.github.io/helm-charts --version 65.8.1 -n monitoring -f monitoring-values.yaml --wait --timeout 600s` | Install the monitoring stack; requires capacity and the credential Secret. |
| `kubectl apply --dry-run=server -f bankapp-service.yaml -f bankapp-servicemonitor.yaml` | Validate selector/port resources against installed monitoring CRDs. |
| `kubectl apply -f bankapp-service.yaml -f bankapp-servicemonitor.yaml` | Apply the labeled Service and named-port scrape target. |
| `kubectl get pods,pvc,hpa -n bankapp; kubectl get pods -n monitoring; kubectl get nodes` | Run workload, storage and infrastructure checks. |
| `kubectl exec -n bankapp deploy/ollama -- ollama list` | Verify the actual downloaded chatbot model. |
| `kubectl port-forward svc/bankapp-service -n bankapp 8080:8080` | Loopback app access; stop with Ctrl-C. |
| `curl --fail http://127.0.0.1:8080/actuator/health; curl --fail http://127.0.0.1:8080/actuator/prometheus` | Verify health and exposed application metrics through the port forward. |
| `kubectl port-forward svc/monitoring-grafana -n monitoring 3000:80` | Inspect Grafana dashboards; stop with Ctrl-C. |
| `kubectl port-forward svc/monitoring-kube-prometheus-prometheus -n monitoring 9090:9090` | Inspect scrape targets and execute the report's queries; stop with Ctrl-C. |
| `helm uninstall monitoring -n monitoring` | Destructive deletion of the exact lab monitoring release. |
| `kubectl delete -f ../day-82/gateway.yaml; kubectl delete namespace bankapp monitoring` | Destructive lab data/workload cleanup after backup/confirmation. |
| `terraform -chdir=../day-81/terraform destroy` | Destroy the exact lab Terraform stack after cloud-created services/storage are released. |
