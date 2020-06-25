from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Movie, Genre, Quality, Director,
                     Subtitles, Rating, Actor, Reviews, MovieShots)


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')


class ReviewInline(admin.TabularInline):
    model = Reviews
    readonly_fields = ("name", "email", 'text')
    show_change_link = True
    fieldsets = (
        (None, {
            # "classes": ("collapse",),
            "fields": (("name", "email", 'text', 'parent'),)
        }),
    )


class QualityInline(admin.TabularInline):
    model = Quality
    # readonly_fields = ("quality", "file")
    show_change_link = True


class RatingInline(admin.TabularInline):
    model = Rating
    readonly_fields = ("stars", "rates")
    show_change_link = True
    can_delete = False


class SubtitlesInline(admin.TabularInline):
    model = Subtitles
    extra = 1
    fields = ('language', 'sub_file')
    show_change_link = True
    can_delete = False


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    """Acotrs and directors"""
    list_display = ("name", "born", "get_image")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Image"

# TODO Add MovieShots
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title', 'description', 'year')
    list_display_links = ('title', 'get_image',)
    list_filter = ('year', "genres__title")
    search_fields = ('title', "genres__title")
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('get_image', )
    inlines = [QualityInline, RatingInline, SubtitlesInline]
    save_on_top = True

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    get_image.short_description = "Movie Image"

    fieldsets = (
        ('Main', {
            "fields": (("title", 'year', 'slug'), ('description', 'published', "genres"), )
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


admin.site.register(Quality)
admin.site.register(Subtitles)
admin.site.register(Director)
admin.site.register(MovieShots)


admin.site.site_title = "Torrent movies with subtitles"
admin.site.site_header = 'Torrent'
