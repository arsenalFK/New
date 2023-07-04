from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class News(models.Model):
    class Meta:
        ordering = ['news_date']
    news_title = models.CharField(max_length=255, verbose_name='Заголовок')
    news_text = models.TextField(verbose_name='Текст')
    news_date = models.DateTimeField(auto_now_add=True)
    news_likes = models.IntegerField(default=0)
    news_image = models.ImageField(null=True, blank=True, verbose_name='Додати зображення')

    def __str__(self):
        return self.news_title

class Player(models.Model):

    TYPE_GOALKEEPER = 'Голкіпер'
    TYPE_DEFENDER = 'Захисник'
    TYPE_MIDFIELDER_DEF = 'Полузахист'
    TYPE_MIDFIELDER_ATK = 'Напівнападаючий'
    TYPE_FORWARD = 'Нападаючий'
    TYPE_CHANGE = 'Заміна'
    TYPE_CHOICES = (
        (TYPE_GOALKEEPER, 'Голкіпер'),
        (TYPE_DEFENDER, 'Захисник'),
        (TYPE_MIDFIELDER_ATK, 'Полузахист'),
        (TYPE_MIDFIELDER_DEF, 'Напівнападаючий'),
        (TYPE_FORWARD, 'Нападаючий'),
        (TYPE_CHANGE, 'Заміна'),
    )

    player_image = models.ImageField(null=True, blank=True, help_text='Фото', verbose_name='Додати фото')
    player_img = models.ImageField(null=True)
    player_name = models.CharField(max_length=255, help_text='Імя гравця ', verbose_name='Імя гравця')
    player_sur_name = models.CharField(max_length=255, help_text='Прізвище гравця', verbose_name='Прізвище гравця')
    birth = models.DateField(null=True)
    player_age = models.SmallIntegerField(default=0, help_text='Вік', verbose_name='Вік')
    player_compose = models.ForeignKey('Compose', on_delete=models.CASCADE, default=1, help_text='Склад (I/II)', verbose_name='Склад')
    player_position = models.CharField(max_length=15, choices=TYPE_CHOICES, default=TYPE_CHANGE, help_text='Позиція', verbose_name='Ігрова позиція')
    weight = models.SmallIntegerField(default=0, null=True)
    height = models.SmallIntegerField(default=0, null=True)
    yellow = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Жовті картки',
                                         help_text='Показник голкіпера (мін - 1, макс - 99)')
    red = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Червоні картки',
                                          help_text='Показник нападу (мін - 1, макс - 99)')
    missed = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Пропущено матчів',
                                          help_text='Показник захисту (мін - 1, макс - 99)')
    goals = models.SmallIntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99)], verbose_name='Забито голів',
                                          help_text='Показник забитих мячів (мін - 1, макс - 99)')
    def __str__(self):
        return self.player_sur_name

class Compose(models.Model):

    TYPE_I = 1
    TYPE_II = 2
    TYPE_CHOICES = (
        (TYPE_I, 'Перший склад'),
        (TYPE_II, 'Другий склад'),
    )

    compose_name = models.CharField(max_length=255)
    compose = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=TYPE_I)

    def __str__(self):
        return self.compose_name

class PlayerRequest(models.Model):

    player_request_name = models.CharField(max_length=255, verbose_name='Імя')
    player_request_name2 = models.CharField(max_length=255, verbose_name='Прізвище')
    player_request_age = models.SmallIntegerField(default=0, verbose_name='Вік')
    player_request_contacts = models.TextField(verbose_name='Контакти', help_text='Ном.Тел, Viber, WhatsApp, Skype')

    def __str__(self):
        return self.player_request_name2


from django.db import models

class GeeksModel(models.Model):
    title = models.CharField(max_length = 200)
    img = models.ImageField(upload_to = "images/")

    def __str__(self):
        return self.title
