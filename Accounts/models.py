from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class StudyGroupModel(models.Model):
    name = models.CharField(max_length=10, blank=False, null=False, verbose_name=u'Имя группы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Учебная группа'
        verbose_name_plural = u'Учебные группы'


class RExamUserModel(AbstractUser):
    middle_name = models.CharField(max_length=20, blank=True, null=False, verbose_name=u'Отчество')
    study_group = models.ForeignKey(StudyGroupModel, on_delete=models.SET_NULL, null=True, blank=True,
                                    verbose_name=u'Учебная группа')

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = u'Пользователь'
        verbose_name_plural = u'Пользователи'
