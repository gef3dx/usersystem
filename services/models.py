from django.db import models
from users.models import CustomUser


class ServicesGalleryModel(models.Model):
    image = models.ImageField(verbose_name="Картинка", upload_to="upload/")


class ServicesCategoryModel(models.Model):
    name = models.CharField(verbose_name="Категория", max_length=100)
    description = models.CharField(verbose_name="Описание категории", max_length=255)
    slug = models.SlugField(verbose_name="Ссылка категории", unique=True)


class ServicesModel(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=255)
    description = models.TextField(verbose_name="Описание услуги", max_length=1000)
    author = models.ForeignKey(CustomUser, verbose_name="Автор услуги", on_delete=models.CASCADE)
    gallery = models.ForeignKey(ServicesGalleryModel, verbose_name="Фото услуг", on_delete=models.CASCADE)

