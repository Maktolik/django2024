from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Game, Genre

from django.shortcuts import get_object_or_404


def index(request: HttpRequest):
    return render(request, 'shop/index.html')


def games_list(request: HttpRequest):
    context = {
        "games": Game.objects.prefetch_related("genres").all(),
    }

    return render(request, 'shop/games-list.html', context=context)


def game_info(request: HttpRequest, game_id: int):
    context = {
        "game": get_object_or_404(Game, pk=game_id),
    }

    return render(request, 'shop/game-info.html', context=context)