"""config URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

from website.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('passwords/', include('website.passwords.urls')),
    path('users/', include('django.contrib.auth.urls')),
]
