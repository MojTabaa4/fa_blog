# Generated by Django 3.1 on 2020-08-17 14:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200815_0131'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
        migrations.AddField(
            model_name='article',
            name='update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='description',
            field=models.TextField(verbose_name='محتوا'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='زمان انتشار'),
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(max_length=100, unique=True, verbose_name='ادرس مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Published')], max_length=10, verbose_name='وضعیت'),
        ),
        migrations.AlterField(
            model_name='article',
            name='thumbnail',
            field=models.ImageField(upload_to='images', verbose_name='عکس مقاله'),
        ),
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=100, verbose_name='عنوان مقاله'),
        ),
    ]
