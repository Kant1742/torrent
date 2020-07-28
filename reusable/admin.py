from django.contrib import admin

from .models import Collection, Merch


class CollectionInline(admin.TabularInline):
    model = Collection
    readonly_fields = ("get_image",)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')


@ admin.register(Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title',)
    list_display_links = ('title', 'get_image')
    search_fields = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')


@ admin.register(Merch)
class MerchAdmin(admin.ModelAdmin):
    list_display = ('get_image', 'title',)
    list_display_links = ('title', 'get_image')
    search_fields = ('title', 'id')
    prepopulated_fields = {'slug': ('title',)}

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
