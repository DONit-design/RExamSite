from django.db import models

# Create your models here.
from Accounts.models import RExamUserModel


class NewsTypeModel(models.Model):
    name = models.CharField(max_length=15, blank=False, verbose_name=u'Текст новости')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Тип новости'
        verbose_name_plural = u'Типы новостей'


class NewsModel(models.Model):
    header = models.CharField(max_length=40, blank=False, verbose_name=u'Заголовок новости')
    content = models.TextField(blank=False, verbose_name=u'Текст новости')
    image = models.ImageField(upload_to='NewsImages', blank=True, verbose_name=u'Изображение новости')
    type = models.ForeignKey(NewsTypeModel, on_delete=models.SET_NULL, null=True, verbose_name=u'Тип новости')
    date = models.DateTimeField(auto_now_add=True, blank=False, verbose_name=u'Дата')
    author = models.ForeignKey(RExamUserModel, null=True, on_delete=models.SET_NULL, verbose_name=u'Автор')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = u'Новость'
        verbose_name_plural = u'Новости'
        ordering = ['-date']
