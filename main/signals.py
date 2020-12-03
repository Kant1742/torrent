from django.contrib.auth.models import User
from django.core.signals import send_mail
from django.db.models import signals
from django.urls import reverse
from django.urls.exceptions import Http404
from django.shortcuts import redirect


def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_mail(
            'Verify your account',
            'Follow this link to verify your account: '
            'http://localhost:8000%s' % reverse(
                'verify', kwargs={'uuid': str(instance.verification_uuid)}),
            'from@quickpublisher.dev',
            [instance.email],
            fail_silently=False,
        )

signals.post_save.connect(user_post_save, sender=User)

""" 
# after we added task2
from django.db.models import signals
from main.tasks import send_verification_email
 
 
def user_post_save(sender, instance, signal, *args, **kwargs):
    if not instance.is_verified:
        # Send verification email
        send_verification_email.delay(instance.pk)
 
signals.post_save.connect(user_post_save, sender=User)
 """



""" 
# gmail settings configuration.
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '<YOUR_GMAIL_USERNAME>@gmail.com'
EMAIL_HOST_PASSWORD = '<YOUR_GMAIL_PASSWORD>'
EMAIL_PORT = 587
 """


# views.py
def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DosNotExist:
        raise Http404('User does not exist')

    user.is_verified = True
    user.save()

    return redirect('main:home')


# urls.py

    # path('verify/<uuid:uuid>/', verify, name='verify'),
