from django.db.models.signals import pre_migrate, post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User


# django built in pre_migrate signal
@receiver(pre_migrate)
def init(sender, app_config, verbosity, interactive, stdout, using, plan, apps, *args, **kwargs):
    print("--------- This is pre_migrate signal ----------")
    print('sender : ', sender)
    print('app_config : ', app_config)
    print('verbosity : ', verbosity)
    print('iteractive : ', interactive)
    print('stdout : ', stdout)
    print('using : ', using)
    print('plan : ', plan)
    print('apps : ', apps)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')


# django built in post_migrate signal
@receiver(post_migrate)
def init(sender, app_config, verbosity, interactive, stdout, using, plan, apps, *args, **kwargs):
    print("--------- This is post_migrate signal ----------")
    print('sender : ', sender)
    print('app_config : ', app_config)
    print('verbosity : ', verbosity)
    print('iteractive : ', interactive)
    print('stdout : ', stdout)
    print('using : ', using)
    print('plan : ', plan)
    print('apps : ', apps)
    print(f'args : {args}')
    print(f'kwargs : {kwargs}')
