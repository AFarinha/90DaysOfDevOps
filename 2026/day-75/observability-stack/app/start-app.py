"""Enable the lab metrics middleware without modifying the upstream checkout."""
import os,sys
sys.path.insert(0,"/app")
os.environ.setdefault("DJANGO_SETTINGS_MODULE","notesapp.settings")
import notesapp.settings as settings
settings.MIDDLEWARE=["metrics.MetricsMiddleware"]+settings.MIDDLEWARE
from django.core.management import execute_from_command_line
execute_from_command_line(["manage.py","runserver","0.0.0.0:8000","--noreload"])
