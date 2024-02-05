from django.db import models

from apps.tours.models import Tour

# Create your models here.
class Hotel(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Заголовок"
    )
    description = models.CharField(
        max_length=500,
        verbose_name="Описание"
    )
    image = models.ImageField(
        upload_to="hotel_images/",
        verbose_name="Фотография отеля"
    )
    stars = models.PositiveSmallIntegerField(
        default=0, verbose_name="Сколько звезд у отеля"
    )
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE,
        related_name="tour_hotels",
        verbose_name="Тур"
    )

    def __str__(self):
        return self.title 

    class Meta:
        verbose_name = "Отель тура"
        verbose_name_plural = "Отели туров"