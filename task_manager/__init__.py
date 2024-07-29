from pathlib import Path

import sys
import os

from celery import Celery


PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

app = Celery('Smart Rule Engine')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
