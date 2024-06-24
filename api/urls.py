"""
URL configuration for base project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path('v1/games/', views.GamesAPIList.as_view(), name='games-list'),
    path('v1/games/<int:pk>/', views.GamesAPIUpdate.as_view(), name='games-update'),
    path('v1/gamesdel/<int:pk>/', views.GamesAPIDestroy.as_view(), name='games-destroy'),


    path('v1/genres/', views.GenresAPIList.as_view(), name='genres'),
    path('v1/genresdel/<int:pk>/', views.GenresAPIDestroy.as_view(), name='genres-destroy'),
]
