# Generated by Django 2.1.3 on 2018-11-13 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181113_1804'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ('-updated',), 'verbose_name': 'Услуга', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='service',
            name='slug',
            field=models.SlugField(max_length=200, verbose_name='Слаг'),
        ),
    ]
