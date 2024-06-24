from django.contrib import admin

from .models import Game, Genre


admin.site.site_header = 'Makshop Admin'
admin.site.site_title = 'Makshop'
admin.site.index_title = 'Welcome to Makshop Admin'


class GenreInLine(admin.TabularInline):
    model = Genre.games.through


def description_short(obj) -> str | None:
    if obj.description is None or len(obj.description) < 48:
        return obj.description
    return obj.description[:48] + "..."


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    inlines = [
        GenreInLine
    ]
    list_display = 'pk', 'title', description_short, 'release_date', 'size', 'price', 'on_sale'
    list_display_links = 'pk', 'title'
    ordering = 'pk', 'title'


class GameInline(admin.StackedInline):
    model = Game.genres.through


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    inlines = [
        GameInline,
    ]

    list_display = 'pk', 'title', description_short
    list_display_links = 'pk', 'title'



