# Generated by Django 3.1 on 2020-08-22 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20200821_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='is_spacial',
            field=models.BooleanField(default=False, verbose_name='مقاله ویژه'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'پیشنویس'), ('p', 'منتشر شده'), ('i', 'در حال بررسی'), ('b', 'برگشت داده شده')], default='p', max_length=10, verbose_name='وضعیت'),
        ),
    ]