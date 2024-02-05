from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class News(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name='user_news',
        verbose_name = 'Пользаватель'
        
    )
    title = models.CharField(
        max_length=255,
        verbose_name='назвпние новости'
    )
    descritions = models.TextField(
        verbose_name='описание'
    )
    
    image= models.ImageField(
        upload_to='news_image/',
        verbose_name='фото'
    )
    
    create = models.DateField(auto_now_add= True, verbose_name='Дата публикации')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name='Новость'
        verbose_name_plural='Новости'
        
