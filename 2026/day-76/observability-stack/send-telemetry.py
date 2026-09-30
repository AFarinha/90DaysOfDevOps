#!/usr/bin/env python3
"""Send fresh synthetic parent/child spans and a cumulative counter over OTLP HTTP."""
import json,time,urllib.request
now=time.time_ns()
resource={"attributes":[{"key":"service.name","value":{"stringValue":"my-test-service"}}]}
spans=[{"traceId":"aaaabbbbccccdddd1111222233334444","spanId":"1111222233334444","name":"GET /api/notes","kind":2,"startTimeUnixNano":str(now-150000000),"endTimeUnixNano":str(now)}, {"traceId":"aaaabbbbccccdddd1111222233334444","spanId":"5555666677778888","parentSpanId":"1111222233334444","name":"SELECT notes FROM database","kind":3,"startTimeUnixNano":str(now-120000000),"endTimeUnixNano":str(now-20000000)}]
metric={"name":"test_requests_total","sum":{"dataPoints":[{"asInt":"42","startTimeUnixNano":str(now-1000000000),"timeUnixNano":str(now)}],"aggregationTemporality":2,"isMonotonic":True}}
for endpoint,payload in [("traces",{"resourceSpans":[{"resource":resource,"scopeSpans":[{"spans":spans}]}]}),("metrics",{"resourceMetrics":[{"resource":resource,"scopeMetrics":[{"metrics":[metric]}]}]})]:
 req=urllib.request.Request("http://127.0.0.1:4318/v1/"+endpoint,json.dumps(payload).encode(),{"Content-Type":"application/json"})
 with urllib.request.urlopen(req,timeout=10) as response: print(endpoint,response.status,response.read().decode())
