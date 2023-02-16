from django.shortcuts import render, HttpResponse
from signal_app import signals
# Create your views here.


def signal(request):
    signals.notification.send(
        sender="I am your sender", task_id=1234, kwargs=['username', 'rabbi'])
    return HttpResponse('There is no one powerfull then one')
