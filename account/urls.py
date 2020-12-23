from django.contrib.auth import views
from django.urls import path
from .views import (Article_list, Article_Create,
                    Article_Update, Article_Delete, Profile
                    )

app_name = 'account'

urlpatterns = [
    path('', Article_list.as_view(), name='home'),
    path('article/create', Article_Create.as_view(), name='article-create'),
    path('article/update/<int:pk>', Article_Update.as_view(), name='article-update'),
    path('profile', Profile.as_view(), name='profile'),
    path('article/delete/<int:pk>', Article_Delete.as_view(), name='article-delete'),
]
