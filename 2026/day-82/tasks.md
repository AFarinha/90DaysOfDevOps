# Day 82 Tasks

Run from this day's directory in WSL Bash. Commands with placeholders require replacement. Cloud steps are pending where credentials are unavailable. Cleanup deletes disposable resources/data and must target only the reviewed lab.

| Command | What it does |
| --- | --- |
| `export KUBECONFIG="$PWD/../day-81/.runtime/eks-kubeconfig"` | Use the dedicated EKS kubeconfig for the required cloud exercise. For local validation use ../day-84/.runtime/kubeconfig instead. |
| `helm upgrade --install envoy-gateway oci://docker.io/envoyproxy/gateway-helm --version v1.4.0 -n envoy-gateway-system --create-namespace --wait --timeout 180s` | Install the README's Gateway controller; creates CRDs and namespace. |
| `kubectl get crd gateways.gateway.networking.k8s.io; kubectl get pods -n envoy-gateway-system` | Confirm Gateway CRDs and controller readiness. |
| `helm upgrade --install cert-manager cert-manager --repo https://charts.jetstack.io -n cert-manager --create-namespace --set crds.enabled=true --set config.enableGatewayAPI=true --wait` | Install cert-manager after Gateway CRDs and enable Gateway integration. |
| `kubectl apply --dry-run=server -f gateway.yaml -f storage.yaml -f cluster-issuer.yaml` | Validate against installed APIs before creating cloud/storage resources; requires bankapp namespace. |
| `kubectl apply -f storage.yaml -f cluster-issuer.yaml -f gateway.yaml` | After replacing domain/email placeholders, create EBS storage and TLS routing resources. |
| `kubectl get gateway,httproute,backendtrafficpolicy,certificate -n bankapp; kubectl get pvc -n bankapp` | Inspect route/policy acceptance, certificate readiness and bound volumes. |
| `aws ec2 describe-volumes --region us-west-2 --filters Name=tag:kubernetes.io/created-by,Values=ebs.csi.aws.com --query 'Volumes[*].{ID:VolumeId,Size:Size,AZ:AvailabilityZone,State:State}' --output table` | Verify actual EBS volume size, AZ and state. |
| `kubectl exec -n bankapp deploy/mysql -- sh -c 'MYSQL_PWD="$MYSQL_ROOT_PASSWORD" mysql -uroot -e "SHOW DATABASES;"'` | Inspect databases without placing a literal password in command history. |
| `kubectl delete pod -n bankapp -l app=mysql` | Destructive disposable-lab persistence test: restarts MySQL while preserving the PVC; confirm data scope first. |
| `kubectl top nodes; kubectl top pods -n bankapp; kubectl get hpa -n bankapp` | Measure allocatable workload behavior rather than assuming nominal instance capacity. |
| `kubectl apply --dry-run=server -f local-gateway.yaml; kubectl apply -f local-gateway.yaml` | Local alternative only: HTTP Gateway for the day-84 Kind chart; no EBS/NLB/TLS evidence. |
| `kubectl delete -f gateway.yaml; helm uninstall envoy-gateway -n envoy-gateway-system; helm uninstall cert-manager -n cert-manager` | Destructive cleanup of these exact lab resources; release public load balancers before deleting EKS. |
