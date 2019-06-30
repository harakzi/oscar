
from django.contrib import admin
from django.urls import path, include
from oscar.app import application

urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('', application.urls),
]
