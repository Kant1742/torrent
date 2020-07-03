from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import (Movie, Genre, Torrents, Director,
                     Subtitles, Cast, Reviews, MovieShots)


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


# class TorrentsInline(admin.TabularInline):
#     model = Torrents
#     # readonly_fields = ("Torrents", "file")
#     show_change_link = True


# class RatingInline(admin.TabularInline):
#     model = Rating
#     readonly_fields = ("stars", "rates")
#     show_change_link = True
#     can_delete = False


class SubtitlesInline(admin.TabularInline):
    model = Subtitles
    extra = 1
    fields = ('language', 'sub_file')
    show_change_link = True
    can_delete = False


@admin.register(Cast)
class CastAdmin(admin.ModelAdmin):
    """Acotrs and directors"""
    list_display = ("name", "character_name", "url_small_image", "imdb_code")
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = "Image"


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_full', 'year')
    list_display_links = ('title',)
    list_filter = ('year',)
    # list_filter = ('year', "genres__title")
    search_fields = ('title',)
    # search_fields = ('title', "genres__title")
    prepopulated_fields = {'slug': ('title',)}
    # readonly_fields = ('get_image', )
    inlines = [SubtitlesInline]
    save_on_top = True

    # def get_image(self, obj):
    #     return mark_safe(f'<img src={obj.image.url} width="100" height="110"')

    # get_image.short_description = "Movie Image"

    # fieldsets = (
    #     ('Main', {
    #         "fields": (("title", 'year', 'slug'), 'description_full',
    #                    'yt_trailer_code',
    #                    'qualities',
    #                    'genres',
    #                    'background_image',
    #                    'background_image_original',
    #                    'small_cover_image',
    #                    'medium_cover_image',
    #                    'large_cover_image',
    #                    'medium_screenshot_image1',
    #                    'medium_screenshot_image2',
    #                    'medium_screenshot_image3',
    #                    'large_screenshot_image1',
    #                    'large_screenshot_image2',
    #                    'large_screenshot_image3')
    #     }),
    #     # ('Image', {
    #     #     "fields": ("image", "get_image")
    #     # }),
    #     # ("Crew", {
    #     #     "fields": (("cast",),)
    #     # }),
    # )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    """Genres"""
    list_display = ("title",)


@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    """Reviews to a movie"""
    list_display = ("name", "email", "parent", "movie", "id")
    readonly_fields = ("name", "email")


# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     """Movie rating"""
#     list_display = ("movie", "stars", "rates")


admin.site.register(Torrents)
admin.site.register(Subtitles)
admin.site.register(Director)
admin.site.register(MovieShots)


admin.site.site_title = "Torrent movies with subtitles"
admin.site.site_header = 'Torrent'
