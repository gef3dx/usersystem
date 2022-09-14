from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
import os


class CustomUser(AbstractUser):
    def image_upload_to(self, instance=None):
        if instance:
            return os.path.join("Users", self.username, instance)
        return None

    STATUS = (
        ('regular', 'regular'),
        ('subscriber', 'subscriber'),
        ('moderator', 'moderator'),
    )

    email = models.EmailField("Электроная почта", unique=True)
    phone = models.CharField("Телефон", max_length=25)
    status = models.CharField("Статус пользователя", max_length=100, choices=STATUS, default='regular')
    description = HTMLField("Расскажите о себе", blank=True, default="")
    image = models.ImageField("Аватар", default='default/user.png', upload_to=image_upload_to)
    #check = models.DecimalField(verbose_name="Счет", default=0, max_digits=8, decimal_places=2)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class SubscribedUsers(models.Model):
    name = models.CharField("Имя", max_length=100)
    email = models.EmailField("Электроная почта", unique=True, max_length=100)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
