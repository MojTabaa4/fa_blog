from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.utils.html import format_html
from extensions.utils import jalali_converter
from account.models import User

from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment


# my managers
class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')


class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.SET_NULL,
                               related_name='children', verbose_name='زیر دسته')
    title = models.CharField(max_length=100, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس دسته بندی")
    status = models.BooleanField(default=True, verbose_name="ایا نمایش داده شود")
    position = models.IntegerField(verbose_name="اولویت")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ['parent__id', 'position']

    def __str__(self):
        return self.title

    objects = CategoryManager()


class Article(models.Model):
    STATUS_CHOICES = [
        ('d', 'پیشنویس'),  # draft
        ('p', 'منتشر شده'),  # publish
        ('i', 'در حال بررسی'),  # investigation
        ('b', 'برگشت داده شده'),  # back
    ]

    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='articles',
                               verbose_name="نویسنده")
    title = models.CharField(max_length=100, verbose_name="عنوان مقاله")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="ادرس مقاله")
    description = models.TextField(verbose_name="متن مقاله")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی", related_name='articles')
    thumbnail = models.ImageField(upload_to='images', default='default.jpg', verbose_name="عکس مقاله")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    is_special = models.BooleanField(default=False, verbose_name="مقاله ویژه")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='p', verbose_name="وضعیت")
    comments = GenericRelation(Comment)

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('account:home')

    def jpublish(self):
        return jalali_converter(self.publish)

    jpublish.short_description = 'زمان انتشار'

    def category_published(self):
        return self.category.filter(status=True)

    def thumbnail_tag(self):
        return format_html("<img width=100 height=80 style='border-radius: 5px' src='{}'>".format(self.thumbnail.url))

    thumbnail_tag.short_description = 'عکس مقاله'

    def category_to_str(self):
        return '/ '.join([category.title for category in self.category.active()])

    category_to_str.short_description = 'دسته بندی'

    objects = ArticleManager()
