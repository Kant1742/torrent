import random
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View

from .forms import ReviewForm
from .models import Cast, Genre, Movie, Torrents
from .services import get_all_movie_slugs

class MovieTestListView(ListView):
    model = Movie
    template_name = 'main/movie_test_list.html'
    queryset = Movie.objects.filter(
        Q(download_count__gte=10000) & Q(rating__gte=7) & Q(year__gte=1995)).order_by('-rating')[:25]

    def get_queryset(self):
        context = super().get_queryset()[:4]

        # похую, сколько жанров у фильма

        # добавляет 2 запроса (context[0] и .count())
        # print(context[0].genres.all().count())

        # добавляет тоже 2 запроса. Схуя ли? Без понятия
        # INNER JOIN и второй запрос WHERE
        # print(context[0].genres.all())

        # тоже + 2 запроса (where id и еще один select)
        # похую, сколько жанров
        for i in context[1].genres.all():
            print(i)

        # 3 запроса, так как обращаемся к context[0]
        # first_movie_genres = context[0].genres.all()
        # second_movie_collection = context[1].genres.all()
        # third_movie_genres = context[2].genres.all()

        # + еще 2 запроса
        # some_filter = first_movie_genres[0]
        # some_filter = first_movie_genres[1]
        # print(second_movie_collection)

        # Не делает запросы, так как нет ничегов collection
        # KEKWait. Делает 2 запроса, когда больше нет никакого кода
        # print(context[0].collection.all())
        # print(context[1].collection.all())
        # print(context[2].collection.all())
        return context



class MovieListView(ListView):
    # Buil-in template filter "random"
    model = Movie
    queryset = Movie.objects.filter(
        Q(download_count__gte=10000) & Q(rating__gte=7) & Q(year__gte=1995)).order_by('-rating')
    paginate_by = 4
    template_name = 'main/movie_list.html'

    """ 
    def check_sprinkles(request):
        if request.user.can_sprinkle or request.user.is_staff:
            # By adding this value here it means our display templates
            # can be more generic. We don't need to have
            # {% if request.user.can_sprinkle or request.user.is_staff %}
            # instead just using
            # {% if request.can_sprinkle %}

            request.can_sprinkle = True
            return request
            # Return a HTTP 403 back to the user
        raise PermissionDenied 
    
    """


    def check_user_is_staff(self):
        from django.core.exceptions import PermissionDenied
        
        # if not self.request.user.is_staff:  # 403 Forbidden
        if self.request.user.is_staff:
            # By adding this value here it means our display templates
            # can be more generic. We don't need to have
            # {% if request.user.can_sprinkle or request.user.is_staff %}
            # instead just using
            # {% if request.check_user_is_staff %}

            # request.check_user_is_staff = True
            print('ALOOOOOOOOOOOO')
            return self.request
            # Return a HTTP 403 back to the user
        raise PermissionDenied

    def all_filtered_ids(self, object_list=queryset):  # (?) what's the point?
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

    # the same as above?
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
        # we have 2 exactly the same methods -> 2 times more queries
        context = super().get_context_data(*args, **kwargs)
        context['stored_movies'] = self.random_movies()
        context['random_popular_movies'] = self.random_popular_movies()
        context['check_user_is_staff'] = self.check_user_is_staff()
        # print(self.model.objects.all())
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


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class MovieDetailView(DetailView):
    model = Movie
    template_name = 'main/movie_detail_yts.html'

    def views_counter(self, movie_slug):
        """ Increase `download_count` by 1 every refresh of the page.
        """
        movie = get_object_or_404(Movie, slug=movie_slug)
        movie.download_count += 1  # We will use 'download_count' by now
        movie.save()
        return movie

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        movie = context['movie']
        # ip = get_client_ip(self.request)
        context['movie_cast'] = Cast.objects.filter(movie=movie)
        context['download_count'] = self.views_counter(movie.slug)
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


# core/views.py
class TitleSearchMixin:

    def get_queryset(self):
        # fetch the queryset from the parent's get_queryset
        queryset = self.super().get_queryset()

        # Get the `q` GET parameter
        q = self.request.GET.get('q')
        if q:
            # return a filtered queryset
            return queryset.filter(title__icontains=q)
        # no `q` if specified, so we return queryset
        return queryset

# # flavors/views.py
# class FlavorListView(TitleSearchMixin, ListView):
#     model = Flavor


# class IceCreamStoreListView(TitleSearchMixin, ListView):
#     model = Store
