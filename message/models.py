from django.db import models
from django.utils import timezone
from users.models import CustomUser


class ThreadModel(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    receiver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')


class MessageModel(models.Model):
    thread = models.ForeignKey(ThreadModel, related_name='+', on_delete=models.CASCADE, blank=True, null=True)
    sender_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    receiver_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='+')
    body = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='uploads/message_photos', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)
    is_read = models.BooleanField(default=False)
