
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls.conf import include

from blog.models import Post
from .views import home,post,contact,about

urlpatterns = [
    path('',home),
    path('blog/<slug:url>',post),
    path('contact/',contact),
    path('about/',about)
]
