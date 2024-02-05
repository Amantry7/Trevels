from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название тура"
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание тура"
    )
    date = models.DateTimeField(
        verbose_name="Дата тура"
    )
    price = models.SmallIntegerField(
        verbose_name="Цена тура"
    )

    def __str__(self):
        return self.title 
    
    class Meta:
        verbose_name = "Тур"
        verbose_name_plural = "Туры"