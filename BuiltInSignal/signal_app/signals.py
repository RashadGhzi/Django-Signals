from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed
from django.dispatch import receiver
from django.contrib.auth.models import User

# django built_in log in signal


@receiver(user_logged_in, sender=User)
def login(sender, request, user, **kwargs):
    print("-------- This is user_logged_in Signal ---------")
    print('sender : ', sender)
    print('request : ', request)
    print('user : ', user)
    print('kwargs : ', kwargs)

# django built_in log out signal


@receiver(user_logged_out, sender=User)
def login(sender, request, user, **kwargs):
    print("-------- This is user_logged_out Signal ---------")
    print('sender : ', sender)
    print('request : ', request)
    print('user : ', user)
    print('kwargs : ', kwargs)


# django built_in log in failed signal
@receiver(user_login_failed)
def login(sender, credentials, request, **kwargs):
    print("-------- This is user_login_failed Signal ---------")
    print('sender : ', sender)
    print('request : ', request)
    print('credentials : ', credentials)
    print('kwargs : ', kwargs)
