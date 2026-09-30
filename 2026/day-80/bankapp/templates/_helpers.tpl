{{- define "bankapp.fullname" -}}
{{- printf "%s-bankapp" .Release.Name | trunc 50 | trimSuffix "-" -}}
{{- end -}}
{{- define "bankapp.labels" -}}
app.kubernetes.io/name: bankapp
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | quote }}
{{- end -}}
{{- define "bankapp.secretName" -}}
{{- default (printf "%s-secret" (include "bankapp.fullname" .)) .Values.secrets.existingSecret -}}
{{- end -}}
{{- define "bankapp.mysqlHost" -}}
{{- if .Values.mysql.enabled -}}
{{- printf "%s-mysql" (include "bankapp.fullname" .) -}}
{{- else -}}
{{- required "config.externalMysqlHost is required when mysql.enabled=false" .Values.config.externalMysqlHost -}}
{{- end -}}
{{- end -}}
