from pathlib import Path

import sys
import os
import django

from celery import Celery
from celery.schedules import crontab


PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

app = Celery('Smart Rule Engine')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


app.conf.beat_schedule = {
    'extract_all_integrations_device_data_task_every_minute': {
        'task': 'core.tasks.iot_platform.handler.extract_all_integrations_device_data_task',
        'schedule': crontab(minute='*'),
    },
}
