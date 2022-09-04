import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MainPortal.settings')

app = Celery('MainPortal')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'mailing_subscribers': {
        'task': 'news.tasks.mailing_subscribers',
        'schedule': crontab(day_of_week='monday', hour=8, minute=0)
    }
}

app.autodiscover_tasks()