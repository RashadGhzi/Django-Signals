from django.db.models.signals import pre_delete, post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User


# django built in pre delete signal
@receiver(pre_delete)
def init(sender, instance, using, origin, *args, **kwargs):
    print("--------- This is pre_delete signal ----------")
    print('sender : ', sender)
    print('instance : ', instance)
    print('using : ', using)
    print('origin : ', origin)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')


# django built in post delete signal
@receiver(post_delete)
def init(sender, instance, using, origin, *args, **kwargs):
    print("--------- This is post_delete signal ----------")
    print('sender : ', sender)
    print('instance : ', instance)
    print('using : ', using)
    print('origin : ', origin)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
