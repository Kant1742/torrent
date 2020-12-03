import os 

from celery import Celery


# мы устанавливаем переменную окружения DJANGO_SETTINGS_MODULE
# по умолчанию для запуска через командную строку celery:
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'torrent.settings')

app = Celery('torrent')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request}')
