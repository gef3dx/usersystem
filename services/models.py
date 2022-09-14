from django.db import models
from tinymce.models import HTMLField

from users.models import CustomUser
from mptt.models import MPTTModel, TreeForeignKey


class ServicesGalleryModel(models.Model):
    imgname = models.CharField(verbose_name="Имя картинки")
    image = models.ImageField(verbose_name="Картинка", upload_to="upload/")

    def __str__(self):
        return self.imgname

    class Meta:
        verbose_name = "Фото для услуги"
        verbose_name_plural = "Фотографии для услуг"


class ServicesCategoryModel(MPTTModel):
    name = models.CharField(verbose_name="Категория", max_length=100)
    description = models.CharField(verbose_name="Описание категории", max_length=255)
    parent = TreeForeignKey('self', verbose_name="Категория", on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория усуги"
        verbose_name_plural = "Категории услуг"

class ServicesModel(models.Model):
    title = models.CharField(verbose_name="Название услуги", max_length=255)
    description = HTMLField("Описание услуги", blank=True, default="")
    author = models.ForeignKey(CustomUser, verbose_name="Автор услуги", on_delete=models.CASCADE)
    gallery = models.ForeignKey(ServicesGalleryModel, verbose_name="Фотогалерея", on_delete=models.CASCADE)
    category = TreeForeignKey(ServicesCategoryModel, verbose_name="Категория", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"