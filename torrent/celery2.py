import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torrent.settings')

app = Celery('torrent')
app.config_from_object('django.conf:settings')

app.autodiscover_tasks()


# Scheduled task
# app.conf.beat_schedule = {
#     'send-report-every-single-minute': {
#         'task': 'torrent.tasks.send_view_count_report',
#         'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
#     },
# }

# $ celery -A quick_publisher beat

""" 

# REDIS related settings 
REDIS_HOST = 'localhost'
REDIS_PORT = '6379'
BROKER_URL = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600} 
CELERY_RESULT_BACKEND = 'redis://' + REDIS_HOST + ':' + REDIS_PORT + '/0'
 """
 