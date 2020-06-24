from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Movie, Genre, File, Quality, Director,
                     Subtitles, Rating, Actor, Reviews)


class ReviewInline(admin.TabularInline):
    model = Reviews
    extra = 1
    readonly_fields = ("name", "email")


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Acotrs and directors"""
    list_display = ("name", "born", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Image"

# TODO Add rating, quality, files
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description', 'year')
    list_display_links = ('title', 'get_image',)
    list_filter = ('year', "genres__title")
    search_fields = ('title', "genres__title")
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image', )
    inlines = [ReviewInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Movie Image"

    fieldsets = (
        ('Main', {
            "fields": ("title", 'year', "genres", 'description', 'published', 'slug')
        }),
        ('Image', {
            "fields": ("image", "get_image")
        }),
        ("Crew", {
            "fields": (("actors", "directors"),)
        }),
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genres"""
    list_display = ("title", "slug")


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Reviews to a movie"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    """Movie rating"""
    list_display = ("movie", "stars", "rates")


admin.site.register(File)
admin.site.register(Quality)
admin.site.register(Subtitles)
admin.site.register(Director)


admin.site.site_title = "Torrent movies with subtitles"
admin.site.site_header = 'Torrent'
