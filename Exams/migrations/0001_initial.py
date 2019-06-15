# Generated by Django 2.2.2 on 2019-06-12 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя экзамена')),
                ('description', models.TextField(blank=True, verbose_name='Описание экзамена')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата создания')),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Экзамен',
                'verbose_name_plural': 'Экзамены',
            },
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Имя предмета')),
            ],
            options={
                'verbose_name': 'Предмет',
                'verbose_name_plural': 'Предметы',
            },
        ),
        migrations.CreateModel(
            name='QuestionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.TextField(verbose_name='Текст вопроса')),
                ('question_image', models.ImageField(blank=True, upload_to='QuestionImages', verbose_name='Изображение вопроса')),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.ExamModel', verbose_name='Экзамен')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.AddField(
            model_name='exammodel',
            name='subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Exams.SubjectModel', verbose_name='Предмет'),
        ),
        migrations.CreateModel(
            name='AnswerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.TextField(verbose_name='Текст ответа')),
                ('answer_image', models.ImageField(blank=True, upload_to='AnswerImages', verbose_name='Изображение ответа')),
                ('its_answer', models.BooleanField(blank=True, default=False, verbose_name='Правильный ответ?')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exams.QuestionModel', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
