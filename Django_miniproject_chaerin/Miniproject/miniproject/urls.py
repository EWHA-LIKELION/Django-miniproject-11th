"""
URL configuration for miniproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import mini.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('',mini.views.home ,name='home'),
    path('post/<int:post_id>',mini.views.detail,name="detail"),
    path('<int:pk>/',mini.views.week,name="Week"),
    path('new/',mini.views.new,name="new"),
    path('create/',mini.views.create,name="create"),
    path('delete/<int:post_id>',mini.views.delete,name="delete"),
    path('update_page/<int:post_id>',mini.views.update_page,name="update_page"),
    path('update/<int:post_id>',mini.views.update,name="update"),
    path('<int:post_id>/comment',mini.views.add_comment,name="add_comment"),
    path('update_comment_page/<int:comment_id>',mini.views.update_comment_page,name="update_comment_page"),
    path('update_comment/<int:post_id>/<int:comment_id>',mini.views.update_comment,name="update_comment"),
    path('delete_comment/<int:post_id>/<int:comment_id>',mini.views.delete_comment,name="delete_comment"),
    path('search', mini.views.search, name="search"), #검색기능 추가
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) #이미지 추가를 위해
