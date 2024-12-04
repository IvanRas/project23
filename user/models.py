from django.db import models

# Create your models here.


class CustomUser(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    email = models.EmailField(max_length=250, verbose_name='Email ', help_text='Введите Email', unique=True),
    image = models.ImageField(upload_to='product/photo', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузити фотографию')
    phone_number = models.IntegerField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона', blank=True, null=True)
    created_at = models.DateField(verbose_name='дата создания', help_text='Введите датe создания', blank=True)
    region = models.CharField(max_length=100, verbose_name='Страна', help_text='Введите страны')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пользователь'
