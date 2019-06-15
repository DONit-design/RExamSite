from django.db import models

# Create your models here.
from Accounts.models import RExamUserModel


class SubjectModel(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'Имя предмета')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Предмет'
        verbose_name_plural = u'Предметы'


class ExamModel(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'Имя экзамена')
    description = models.TextField(verbose_name=u'Описание экзамена', blank=True)
    author = models.ForeignKey(RExamUserModel, on_delete=models.SET_NULL, verbose_name=u'Автор', null=True)
    date = models.DateField(auto_now_add=True, verbose_name=u'Дата создания')
    subject = models.ForeignKey(SubjectModel, on_delete=models.SET_NULL, null=True, verbose_name=u'Предмет')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'Экзамен'
        verbose_name_plural = u'Экзамены'


class QuestionModel(models.Model):
    question_text = models.TextField(verbose_name=u'Текст вопроса')
    question_image = models.ImageField(upload_to='QuestionImages', blank=True, verbose_name=u'Изображение вопроса')
    exam = models.ForeignKey(ExamModel, on_delete=models.CASCADE, verbose_name=u'Экзамен')

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'


class AnswerModel(models.Model):
    answer_text = models.TextField(verbose_name=u'Текст ответа')
    answer_image = models.ImageField(upload_to='AnswerImages', blank=True, verbose_name=u'Изображение ответа')
    its_answer = models.BooleanField(verbose_name=u'Правильный ответ?', blank=True, default=False)
    question = models.ForeignKey(QuestionModel, on_delete=models.CASCADE, verbose_name=u'Вопрос')

    def __str__(self):
        return self.answer_text

    class Meta:
        verbose_name = u'Ответ'
        verbose_name_plural = u'Ответы'
