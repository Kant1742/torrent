from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie, Genre, Quality
from .forms import ReviewForm
from django.http import HttpResponse


class GenreYear:
    """Genres and years"""

    def get_genres(self):
        return Genre.objects.all()

    def get_years(self):
        return Movie.objects.values("year")


class MovieListView(ListView):
    model = Movie
    paginate_by = 25

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     movies = Movie.objects.filter().first()
    #     context['genres'] = Genre.objects.filter(movie__title=movies.title)

    #     return context


class MovieDetailView(GenreYear, DetailView):
    model = Movie

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     movie = get_object_or_404(Movie)
    #     if movie.quality.quality_360:
    #         context['quality_360'] = movie.quality.quality_360
    #     if movie.quality.quality_480:
    #         context['quality_480'] = movie.quality.quality_480
    #     if movie.quality.quality_720:
    #         context['quality_720'] = movie.quality.quality_720
    #     if movie.quality.quality_1080:
    #         context['quality_1080'] = movie.quality.quality_1080
    #     return context


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