# Generated by Django 2.1.3 on 2018-11-13 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20181113_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='photo',
            field=models.ImageField(default='../static/images/not_found.jpg', upload_to='services/%Y', verbose_name='Картинка услуги'),
        ),
    ]
