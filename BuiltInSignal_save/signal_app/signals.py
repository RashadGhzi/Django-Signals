from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


# django built in pre save signal
@receiver(pre_save)
def init(sender, instance, raw, using, update_fields, *args, **kwargs):
    print("--------- This is pre_save signal ----------")
    print('sender : ', sender)
    print('instance : ', instance)
    print('raw : ', raw)
    print('using : ', using)
    print('update_fields : ', update_fields)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')

# django built in post save signal


@receiver(post_save)
def init(sender, instance, created, raw, using, update_fields, *args, **kwargs):
    print("--------- This is post_save signal ----------")
    print('sender : ', sender)
    print('instance : ', instance)
    print('created : ', created)
    print('raw : ', raw)
    print('using : ', using)
    print('update_fields : ', update_fields)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
