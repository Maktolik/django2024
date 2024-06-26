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

from . import views, admin

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('app/', views.games_list, name='games-list'),
    path('app/<int:game_id>/', views.game_info, name='game-info'),
    # path('genre/', views.genre, name='genres-list'),
    path('genre/<int:genre_id>/', views.genre_info, name='genre-info'),
    path('random/', views.random_game, name='random-game'),
]
