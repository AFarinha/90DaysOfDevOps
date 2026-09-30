# Day 79 - Custom AI-BankApp Chart

## Chart and raw-manifest mapping

`bankapp/` contains chart metadata, values, helper templates, configuration, secret/storage resources, three deployments, services, HPA and optional Gateway/HTTPRoute. Namespace creation is handled by Helm's `--create-namespace`. ClusterIssuer and Gateway controller installation remain cluster-level prerequisites; this chart does not install them.

| Raw resource | Chart implementation |
| --- | --- |
| `configmap.yml`: fixed mysql-service and ollama-service names | ConfigMap derives release-scoped names and permits an external MySQL host/override Ollama URL |
| `secrets.yml`: fixed base64 strings | Existing Secret by default; optional generated Secret requires privately supplied password values |
| `bankapp-deployment.yml`: fixed image, replicas and init endpoints | Configurable image/resources; replica count is omitted for HPA; init endpoints follow release names |
| `mysql-deployment.yml`: early liveness check | Added startup probe so initial database creation is not killed by liveness |
| `ollama-deployment.yml`: model pull and probes | Preserves postStart model pull and model-readiness check |
| `pv.yml` and `pvc.yml` | Optional cluster StorageClass plus conditional per-release PVCs |

## Values

| Section | Configuration |
| --- | --- |
| bankapp | Image/tag, replica count, requests/limits, service and HPA thresholds |
| mysql | Component enable flag, image/resources and persistence |
| ollama | Component enable flag, image/model/resources and persistence |
| config | Database name, external MySQL host and optional Ollama URL override |
| secrets | Existing Secret name, username and optional passwords for generated Secret |
| storageClass | Whether to create a cluster-scoped class and its provisioner |
| gateway | Enable flag, hostname, class and optional existing TLS certificate |

See `bankapp/values.yaml` for the complete values, rather than duplicating them here. Defaults use the observed reference BankApp image tag `1c7cb0e`, Kind `standard` storage and an existing Secret. Image existence/readiness is established only by runtime evidence. MySQL defaults use root to match the source app: this is a lab choice, not least-privilege production configuration.

Disabling MySQL removes its Deployment, Service and PVC and requires `config.externalMysqlHost`. Disabling Ollama removes its Deployment, Service, PVC and app wait init container. The application may still attempt an Ollama request when the chatbot feature is used; disabling infrastructure is not a guarantee that the application code disables that feature.

## Go templates

| Syntax | Purpose |
| --- | --- |
| `.Values.bankapp.image.tag` | Read configured value |
| `if` / `end` | Conditional resources or fields |
| `range` | Iterate a list or map |
| `with` | Set the current context to a nonempty value |
| `include` | Return helper output for piping |
| `toYaml` / `nindent` | Encode and indent structured resources |
| `b64enc` | Encode Secret data; base64 is not encryption |
| `required` | Fail rendering when essential external configuration is absent |

Names are release-scoped; service selectors match the pod labels. Helpers cap names to leave space for resource suffixes. Preserve Secret/PVC identity across upgrades and rotate secrets deliberately.

## Validation and lessons

`helm lint` passed. The default template rendered ten resources. Optional-component checks removed all MySQL/Ollama resources and retained a two-replica app against an external DB hostname. Server-side dry-run accepted all default manifests in the lab namespace. Packages were generated only into ignored runtime storage.

Real deployment initially exceeded its timeout while pulling Ollama. An early MySQL liveness restart corrupted its disposable initialization; a startup probe and a fresh release corrected this, and the replacement MySQL reached Ready. The same corrected core templates then ran successfully through the day-80 chart upgrade: the BankApp and database were Ready, `/actuator/health` returned HTTP 200 with UP, `/login` returned Login - BankApp with a form, and `ollama list` showed tinyllama:latest (637 MB). A further BankApp startup probe protects the observed 116-second boot. `validation.md` records that shared integration evidence; the successful full deployment used chart 0.2.0.
