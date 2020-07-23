from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse

from .models import Movie, Genre, Torrents, Cast
from .forms import ReviewForm


class GenreYear:
    """Genres and years"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.values("year")


class MovieListView(ListView):
    # model = Movie
    # TODO use Q for filtering using 2 fields
    queryset = Movie.objects.order_by('-rating')
    paginate_by = 8

    def get_queryset(self):
        queryset = Movie.objects.filter(
            Q(download_count__gte=10000)).order_by('-rating')
        return queryset

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     movies = Movie.objects.filter().first()
    #     context['genres'] = Genre.objects.filter(movie__title=movies.title)

    #     return context


class SearchResultsView(ListView):
    model = Movie
    template_name = 'search_results.html'
    paginate_by = 15

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(
            (Q(title__icontains=query) | Q(year__icontains=query)
             & Q(download_count__gte=100000))
        ).order_by('-rating')
        # if len(object_list) < self.paginate_by:
        #     object_list = Movie.objects.filter(
        #         (Q(title__icontains=query) | Q(year__icontains=query)
        #          & Q(download_count__gte=50000)))
        return object_list


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    template_name = 'main/movie_detail_yts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        movie = context['movie']
        context['movie_cast'] = Cast.objects.filter(movie=movie)
        cast = context['movie_cast']
        print(f'\n\n{cast[0].character_name}\n\n')
        return context


class AddReview(View):
    """Reviews"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
