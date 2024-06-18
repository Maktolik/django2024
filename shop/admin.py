from django.contrib import admin

from .models import Game, Genre


class GenreInLine(admin.TabularInline):
    model = Genre.games.through


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [
        GenreInLine
    ]
    list_display = 'pk', 'title', 'description_short', 'release_date', 'size', 'price', 'on_sale'
    list_display_links = 'pk', 'title'
    ordering = 'pk', 'title'

    def description_short(self, obj: Game) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


class GameInline(admin.StackedInline):
    model = Game.genres.through


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    inlines = [
        GameInline,
    ]

    list_display = 'pk', 'title'
    list_display_links = 'pk', 'title'



