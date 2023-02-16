from django.core.signals import request_started, request_finished, got_request_exception
from django.dispatch import receiver
from django.contrib.auth.models import User

# django built in request_started signal


@receiver(request_started)
def init(sender, environ, *args, **kwargs):
    print("--------- This is request_started signal ----------")
    print('sender : ', sender)
    print('environ : ', environ)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')


# django built in request_finished signal
@receiver(request_finished)
def init(sender, *args, **kwargs):
    print("--------- This is request_finished signal ----------")
    print('sender : ', sender)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')

# django built in got_request_exception signal


@receiver(got_request_exception)
def init(sender, request, *args, **kwargs):
    print("--------- This is got_request_exception signal ----------")
    print('sender : ', sender)
    print('request : ', request)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
