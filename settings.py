import os
from dotenv import load_dotenv

load_dotenv()

AI_API_KEY = os.getenv('AI_API_KEY')
IoT_PLATFORM_API_KEY = os.getenv('IoT_PLATFORM_API_KEY')
IoT_PLATFORM_BASE_URL = os.getenv('IoT_PLATFORM_BASE_URL')
REDIS_ENDPOINT = os.getenv('REDIS_ENDPOINT', 'localhost')

# CELERY CONFIGURATION
CELERY_BROKER_URL = f'redis://{REDIS_ENDPOINT}:6379'
CELERY_RESULT_BACKEND = f'redis://{REDIS_ENDPOINT}:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'
CELERY_IMPORTS = (
    'core.tasks.rule_engine.handler',
)
