# Generated by Django 2.2.2 on 2019-06-08 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0003_auto_20190608_1728'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsmodel',
            options={'ordering': ['date'], 'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterField(
            model_name='newsmodel',
            name='header',
            field=models.CharField(max_length=40, verbose_name='Заголовок новости'),
        ),
    ]
