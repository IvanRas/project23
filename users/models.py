from django.db import models

# Create your models here.


class CustomUserCreationForm(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя', help_text='Введите имя')
    email = models.EmailField(unique=True, verbose_name="Эл.почта")
    image = models.ImageField(upload_to='product/photo', blank=True, null=True, verbose_name='фото',
                              help_text='Загрузити фотографию')
    phone_number = models.IntegerField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона', blank=True, null=True)
    country = models.CharField(max_length=40, verbose_name="Страна", blank=True, null=True,
                               help_text="Введите страну проживания")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'пользователь'
