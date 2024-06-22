from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from .models import Game, Genre


def index(request: HttpRequest):
    context = {
        "games": Game.objects.prefetch_related("genres").all(),
    }

    return render(request, 'shop/games-list.html', context=context)