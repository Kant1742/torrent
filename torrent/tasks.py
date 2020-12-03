from celery import group
import smtplib
from datetime import datetime

from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.template import Context, Engine

from celery.schedules import crontab
from torrent.celery import app

# ----------- #
# Schedule a task to send emails every monday.
CELERY_BEAT_SCHEDULE = {
    'monday-statistics-email': {
        'task': 'myproject.apps.statistics.tasks.monday_email',
        'schedule': crontab(day_of_week=1, hour=7)
    }
}
# ----------- #


def render_template(template, context):
    engine = Engine.get_default()
    tmpl = engine.get_template(template)
    return tmpl.render(Context(context))


@celery_app.task(bind=True, default_retry_delay=10 * 60)
def send_mail_task(self, recipients, subject, template, context):
    message = render_template(f'{template}.txt', context)
    html_message = render_template(f'{template}.html', context)
    try:
        send_mail(
            subject=subject,
            message=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=recipients,
            fail_silently=False,
            html_message=html_message
        )
    except smtplib.SMTPException as ex:
        self.retry(exc=ex)
# ----------- #


# ----------- #
send_mail_task.apply_sync(
    (('noreply@example.com', ), 'Celery cookbook test', 'test', {}),
    countdown=15 * 60  # every 15 minutes
)
# ----------- #


# ----------- #
send_mail_task.apply_sync(
    (('noreply@example.com', ), 'Celery cookbook test', 'test', {}),
    eta=datetime(2020, 5, 20, 7, 0)  # 7 часов утра 20 мая.
)
# ----------- #


# ----------- #
CELERY_TASK_ROUTERS = {
    'myproject.apps.mail.tasks.send_mail_task': {'queue': 'mail', }
}
# ----------- #


# ----------- #
@celery_app.task
def send_good_morning_mail_task(offset=0, limit=100):
    users = User.objects.filter(is_active=True).order_by('id')
    for user in users:
        send_good_morning_mail_task(user)

    if len(users) >= limit:
        send_good_morning_mail_task.delay(offset + limit, limit)
# ----------- #


# ----------- #
@celery_app.task
def calculate_service_provider_task(user_id, provider_id):
    user = User.objects.get(pk=user_id)
    provider = ServiceProvider.objects.get(pk=provider_id)
    return calculate_service_provider(user, provider)


@celery_app.task
def find_best_service_provider_for_user(user_id):
    user = User.objects.get(pk=user_id)
    providers = ServiceProvider.objects.related_to_user(user)
    calc_group = group([
        calculate_service_provider_task.s(user.pk, provider.pk)
        for provider in providers
    ]).apply_async()
    return calc_group

""" 
def view(request):
    find_job = find_best_service_provider_for_user.delay(request.user.pk)

    # do other stuff

    calculations_results = find_job.get().join()
    
    # process calculations_results and send response
 """
# ----------- #
 