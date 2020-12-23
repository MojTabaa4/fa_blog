from django.contrib import admin
from .models import Article, Category

admin.site.site_header = 'Moji Admin Panel'


# Admin actions
def make_published(modeladmin, request, queryset):
    row_update = queryset.update(status='p')
    if row_update == 1:
        message_bit = '1 article was'
    else:
        message_bit = '{} articles were'.format(row_update)
    modeladmin.message_user(request, '{} successfully marked as published'.format(message_bit))


def make_draft(modeladmin, request, queryset):
    row_update = queryset.update(status='d')
    if row_update == 1:
        message_bit = '1 article was'
    else:
        message_bit = '{} articles were'.format(row_update)
    modeladmin.message_user(request, '{} successfully marked as draft'.format(message_bit))


make_published.short_description = 'make selected obj as published'
make_draft.short_description = 'make selected obj as draft'


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category_to_str', 'thumbnail_tag', 'slug', 'jpublish','is_special', 'status')
    list_filter = ('publish', 'status', 'author')
    search_fields = ('title', 'description')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['status', '-publish']
    actions = [make_published, make_draft]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'parent', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
