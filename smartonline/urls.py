"""smartonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,re_path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken import views
from .static_views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="Home"),
    re_path(r'^chambres/',include('chambres.urls')),
    path('api-auth/', views.obtain_auth_token,name="obtain_auth_token"),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header='Administration de la maison'
