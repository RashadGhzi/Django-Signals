from django.dispatch import Signal, receiver
notification = Signal()


@receiver(notification)
def custom_signal(sender, task_id, **kwargs):
    print('Sender : ', sender)
    print('Task ID : ', task_id)
    print(f"kwargs : {kwargs}")
