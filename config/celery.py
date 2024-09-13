from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('config',
             broker='redis://redis:6379/0',
             backend='redis://localhost:6379/0')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Automatically discover tasks from your installed apps
app.autodiscover_tasks()

# Celery Config
app.conf.broker_url = os.environ.get('CELERY_BROKER_URL',
                                     'redis://redis:6379/0')
app.conf.result_backend = os.environ.get('CELERY_RESULT_BACKEND',
                                         'redis://redis:6379/0')
