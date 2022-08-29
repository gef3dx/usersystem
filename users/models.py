from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
import os

def get_path_upload_image(file):
    """
    make path of uploaded file shorter and return it
    in following format: (media)/profile_pics/user_1/myphoto_2018-12-2.png
    """
    time = timezone.now().strftime("%Y-%m-%d")
    end_extention = file.split('.')[1]
    head = file.split('.')[0]
    if len(head) > 10:
        head = head[:10]
    file_name = head + '_' + timezone.now().strftime("%h-%m-%s") + '.' + end_extention
    return os.path.join('photos', '{}', '{}').format(time, file_name)


class Photo(models.Model):
    """Фото"""
    name = models.CharField("Имя", max_length=50)
    image = models.ImageField("Фото", upload_to="gallery/")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.image.name = get_path_upload_image(self.image.name)
        super().save(*args, **kwargs)

        # if self.image:
        #     img = Image.open(self.image.path)
        #     if img.height > 200 or img.width > 200:
        #         output_size = (200, 200)
        #         img.thumbnail(output_size)
        #         img.save(self.image.path)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Gallery(models.Model):
    """Галерея"""
    name = models.CharField("Имя", max_length=50)
    photos = models.ManyToManyField(Photo, verbose_name="Фотографии")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    slug = models.SlugField("url", max_length=50, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Галерея"
        verbose_name_plural = "Галереи"

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

    email = models.EmailField("Электроная почта",unique=True)
    phone = models.CharField("Телефон", max_length=25)
    gallery = models.ManyToManyField(Gallery, verbose_name="Галерея")
    status = models.CharField("Статус пользователя",max_length=100, choices=STATUS, default='regular')
    description = HTMLField("Расскажите о себе",blank=True, default="")
    image = models.ImageField("Аватар", default='default/user.jpg', upload_to=image_upload_to)

    def __str__(self):
        return self.username

class SubscribedUsers(models.Model):
    name = models.CharField("Имя",max_length=100)
    email = models.EmailField("Электроная почта",unique=True, max_length=100)
    created_date = models.DateTimeField('Дата создания', default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"

