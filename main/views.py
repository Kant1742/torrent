from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from .services import get_all_movie_slugs
from django.db.models import Max, Min
import random

from .models import Movie, Genre, Torrents, Cast
from .forms import ReviewForm


class MovieListView(ListView):
    model = Movie
    queryset = Movie.objects.filter(
        Q(download_count__gte=10000) & Q(rating__gte=7) & Q(year__gte=1995)).order_by('-rating')
    paginate_by = 4
    template_name = 'main/movie_list.html'

    def all_filtered_ids(self, object_list=queryset):
        # object_list = self.object_list
        ids = []
        obj_iteration = 0
        for i in object_list:
            obj = object_list[obj_iteration]
            obj_id = obj.id
            ids.append(obj_id)
            obj_iteration += 1
        return ids

    def random_popular_movies(self):
        # total_movies = [ids.append(i) for i in object_list]
        ids = self.all_filtered_ids()
        movies = []
        iterations = 0
        while iterations < self.paginate_by:
            rand = random.choice(ids)
            try:
                m = Movie.objects.get(id=rand)
                movies.append(m)
                iterations += 1
            except:
                continue
        return movies

    def random_movies(self):
        ids = self.all_filtered_ids()
        stored_movies = []
        iterations = 0
        while iterations < self.paginate_by:
            rand = random.choice(ids)
            # If we have this movie
            try:
                m = Movie.objects.get(id=rand)
                stored_movies.append(m)
                iterations += 1
            except:
                continue
        return stored_movies

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['stored_movies'] = self.random_movies()
        context['random_popular_movies'] = self.random_popular_movies()
        return context


class LatestMoviesView(ListView):
    queryset = Movie.objects.all().prefetch_related('genres')
    template_name = 'main/latest_movies.html'
    paginate_by = 12


class CastMoviesList(DetailView):
    # model = Cast
    queryset = Cast.objects.all()
    template_name = 'main/cast_movies_list.html'


class SearchResultsView(ListView):
    # model = Movie
    template_name = 'main/search_results.html'
    paginate_by = 16

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.all().prefetch_related('genres', 'cast').filter(
            (Q(title__icontains=query) | Q(year__icontains=query))).order_by('-rating')
        return object_list


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'main/movie_detail_yts.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        movie = context['movie']
        context['movie_cast'] = Cast.objects.filter(movie=movie)
        cast = context['movie_cast']
        return context


class AddReview(LoginRequiredMixin, View):
    """Reviews"""

    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.movie = movie
            form.name = request.user.username
            form.email = request.user.email
            form.save()
        return redirect(movie.get_absolute_url())
