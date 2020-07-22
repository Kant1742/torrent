from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Movie, Genre, Torrents, Cast
from .forms import ReviewForm
from django.http import HttpResponse


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

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #     movies = Movie.objects.filter().first()
    #     context['genres'] = Genre.objects.filter(movie__title=movies.title)

    #     return context


class MovieDetailView(GenreYear, DetailView):
    model = Movie
    template_name = 'main/movie_detail_yts.html'

    # def get_context_data(self, *args, **kwargs):
    # context = super().get_context_data(*args, **kwargs)
    # context['all_cast'] = Cast.objects.all()
    # movie = get_object_or_404(Movie)
    # return context


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
