
# Create your models here.
from django.db import models
import os

class Catalog(models.Model):
    nameobject = models.CharField(max_length=20, help_text = "Название объекта")
    textobject = models.TextField(help_text="Текст объекта")
    type = models.CharField(max_length=20, help_text="Тип объекта",default=None)
    city = models.CharField(max_length=20, help_text="Местоположение объекта",default=None)
    whoseobject = models.CharField(max_length=20, help_text = "За кем объект")
    date = models.DateField()

    def delete(self, *args, **kwargs):
        # Удаляем все связанные фотографии
        for photo in self.photos.all():
            if photo.image:
                if os.path.isfile(photo.image.path):
                    os.remove(photo.image.path)
            photo.delete()
        super().delete(*args, **kwargs)
    def __str__(self):
        return self.nameobject
class Photo(models.Model):
    catalog = models.ForeignKey(Catalog, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')

    def __str__(self):
        return f'Photo for {self.catalog.name}'
