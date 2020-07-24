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


class GenreYear:
    """Genres and years"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.values("year")


class MovieListView(ListView):
    # model = Movie
    queryset = Movie.objects.filter(
        Q(download_count__gte=10000) & Q(rating__gte=7)).order_by('-rating')
    paginate_by = 8
    template_name = 'main/movie_list.html'

    def random_popular_movies(self):
        object_list = self.object_list
        ids = []
        obj_iteration = 0
        for i in object_list:
            obj = object_list[obj_iteration]
            obj_id = obj.id
            ids.append(obj_id)
            obj_iteration += 1
        
        # total_movies = [ids.append(i) for i in object_list]
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
        print(movies)
        return movies

    def random_movies(self):
        # TODO right now these are only random movies without 7+ validation
        max_id = Movie.objects.all().aggregate(max_id=Max("id"))['max_id']
        min_id = Movie.objects.all().aggregate(min_id=Min("id"))['min_id']
        iterations = 0
        stored_movies = []
        while iterations <= 7:
            rand = random.randint(min_id, max_id)
            # If we have this movie
            try:
                m = Movie.objects.get(id=rand)
                # This way of validation is shitty. It doubles number of queries
                stored_movies.append(m)
                iterations += 1
            # In case we don't have this movie
            except:
                continue
        return stored_movies

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['stored_movies'] = self.random_movies()
        context['random_popular_movies'] = self.random_popular_movies()
        return context


class LatestMoviesView(ListView):
    queryset = Movie.objects.all()
    template_name = 'main/latest_movies.html'
    paginate_by = 16


# class GetOneRandomMovie():
#     def get_random3(self):
#         max_id = Movie.objects.all().aggregate(max_id=Max("id"))['max_id']
#         while True:
#             pk = random.randint(1, max_id)
#             movie = Movie.objects.filter(pk=pk).first()
#             if movie:
#                 return movie


class SearchResultsView(ListView):
    model = Movie
    template_name = 'search_results.html'
    paginate_by = 16

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Movie.objects.filter(
            (Q(title__icontains=query) | Q(year__icontains=query)
             & Q(download_count__gte=100000))).order_by('-rating')
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
