import logging

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.template import Context, Template
from django.urls import reverse
from publisher.models import Post
from quick_publisher.celery import app
from torrent.celery2 import app


@app.task
def send_verification_mail(user_id):
    UserModel = get_user_model()
    try:
        user = UserModel.objects.get(pk=user_id)
        send_mail(
            'Verify your QuickPublisher account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse('verify',
                                                kwargs={'uuid': str(user.verification_uuid)}),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )
    except UserModel.DoesNotExist:
        logging.warning(f'User does not exist {user_id}')


# get post views number for author


REPORT_TEMPLATE = """
Here's how you did till now:
 
{% for post in posts %}
        "{{ post.title }}": viewed {{ post.view_count }} times |
 
{% endfor %}
"""


@app.task
def send_view_count_report():
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue

        template = Template(REPORT_TEMPLATE)

        send_mail(
            'Your posts Activity',
            template.render(context=Context({'posts': posts})),
            'from@quickpublisher.dev',
            [user.email],
            fail_silently=False,
        )
