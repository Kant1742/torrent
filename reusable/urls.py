from django.urls import path, include
from django.views.decorators.cache import cache_page

from .views import CollectionListView, CollectionItemsView

app_name = 'reusable'

urlpatterns = [
    path('',
         # One day
     #     cache_page(60*60*24)
         (CollectionListView.as_view()),
         name='collection_list'),
    path('<slug:slug>/',
     #     cache_page(60*60*24*7)
         (CollectionItemsView.as_view()),
         name='collection_items'),
]
