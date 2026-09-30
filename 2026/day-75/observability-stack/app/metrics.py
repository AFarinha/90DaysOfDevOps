"""Small learning exporter using Django and the Python standard library only."""
import threading,time
from django.http import HttpResponse
lock=threading.Lock()
requests_total=0
started=time.time()
class MetricsMiddleware:
    def __init__(self,get_response): self.get_response=get_response
    def __call__(self,request):
        global requests_total
        if request.path == "/metrics":
            with lock: count=requests_total
            body=("# HELP notes_http_requests_total Application requests excluding scrapes.\n"
                  "# TYPE notes_http_requests_total counter\n"
                  f"notes_http_requests_total {count}\n"
                  "# HELP notes_uptime_seconds Seconds since process start.\n"
                  "# TYPE notes_uptime_seconds gauge\n"
                  f"notes_uptime_seconds {time.time()-started}\n")
            return HttpResponse(body,content_type="text/plain; version=0.0.4")
        with lock: requests_total+=1
        return self.get_response(request)
