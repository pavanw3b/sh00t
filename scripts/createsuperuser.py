import os
import django
import sys
from os.path import dirname, abspath

sh00t_path = dirname(dirname(abspath(__file__)))
sys.path.append(sh00t_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sh00t.settings")
django.setup()

from django.contrib.auth.models import User

User.objects.create_superuser('sh00t', 'sh00t@example.com', 'sh00t')
