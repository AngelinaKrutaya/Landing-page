from django.contrib import admin
from django.conf.urls import url
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include, url
urlpatterns = [
    url(r'^$', include('contacts.urls')),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns = [
    url(r'^contact/', views.contact),
    url(r'^thank/$', views.index),
   # url(r'^contact/', views.image,name="image"),
   # url(r'^(?P<image_id>[0-9]+)/', views.image,name="image"),
    ]

