from celery import Celery

app = Celery('Smart Rule Engine')

app.config_from_object('settings', namespace='CELERY')

app.autodiscover_tasks()
