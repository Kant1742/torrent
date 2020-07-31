from django.shortcuts import render
from django.views.generic import ListView, DetailView
from main.models import Movie
from .models import Collection


class CollectionListView(ListView):
    model = Collection
    paginate_by = 4
    template_name = 'reusable/collection_list.html'


class CollectionItemsView(DetailView):
    model = Collection
    template_name = 'reusable/collection_items.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        return context
