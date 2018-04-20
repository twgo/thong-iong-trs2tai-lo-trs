"""tsuan2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from kai3bin7.views import thong2tai5, thuan5iap8, thong2tai5han3


urlpatterns = [
    #     path('admin/', admin.site.urls),

    path('', thuan5iap8),
#     path('thong2tai5', thong2tai5),
    path('thong2tai5han3', thong2tai5han3),

]
