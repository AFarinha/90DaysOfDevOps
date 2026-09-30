"""Initialize the disposable capstone site through its HTTP installation wizard."""
import os
import urllib.parse
import urllib.request

base = os.environ["WORDPRESS_URL"].rstrip("/")
with urllib.request.urlopen(base + "/wp-admin/install.php?step=1", timeout=30) as response:
    page = response.read().decode()
if "weblog_title" not in page:
    raise RuntimeError("Expected an uninitialized WordPress installation wizard")
form = {
    "weblog_title": "Day 60 Kubernetes Capstone",
    "user_name": "capstone-admin",
    "admin_password": os.environ["WORDPRESS_ADMIN_PASSWORD"],
    "admin_password2": os.environ["WORDPRESS_ADMIN_PASSWORD"],
    "admin_email": "admin@example.invalid",
    "blog_public": "0",
    "pw_weak": "1",
    "Submit": "Install WordPress",
    "language": "en_US",
}
request = urllib.request.Request(
    base + "/wp-admin/install.php?step=2",
    data=urllib.parse.urlencode(form).encode(),
)
with urllib.request.urlopen(request, timeout=90) as response:
    result = response.read().decode()
if "Success!" not in result:
    raise RuntimeError("WordPress installation did not report success")
print("WordPress HTTP installation wizard completed; credentials were not printed")
