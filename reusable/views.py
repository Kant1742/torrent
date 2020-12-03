from django.shortcuts import render
from django.views.generic import DetailView, ListView
from main.models import Movie

from .models import Collection


class CollectionListView(ListView):
    model = Collection
    paginate_by = 8
    template_name = 'reusable/collection_list.html'


class CollectionItemsView(DetailView):
    # model = Collection
    queryset = Collection.objects.all().prefetch_related('collection_movies')
    template_name = 'reusable/collection_items.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print('----------------------')
        print(context['object'].id)
        movie_id = context['object'].collection_movies
        # collection_id = context['object'].id
        print('----------------------')
        # movie = Collection.objects.get()
        # for i in context['object']:
        #     print(i)
        # obj = context['object']
        return context
