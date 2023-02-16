from django.db.models.signals import pre_init, post_init
from django.dispatch import receiver
from django.contrib.auth.models import User

# django built in pre init signal


@receiver(pre_init)
def init(sender, *args, **kwargs):
    print("--------- This is pre_init signal ----------")
    print('sender : ', sender)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')


# django built in post init signal
@receiver(post_init)
def init(sender, instance, *args, **kwargs):
    print("--------- This is post_init signal ----------")
    print('sender : ', sender)
    print('instance : ', instance)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
