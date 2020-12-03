from django.urls import include, path
from django.views.decorators.cache import cache_page

from .views import (AddReview, CastMoviesList, LatestMoviesView,
                    MovieDetailView, MovieListView, MovieTestListView,
                    SearchResultsView)

app_name = 'main'

urlpatterns = [
    path('',
         # cache_page(60*60)
         (MovieListView.as_view()),
         name='movie_list'),
    path('test-list/',
         # cache_page(60*60)
         (MovieTestListView.as_view()),
         name='movie_test_list'),
    path('search/',
         # 7 days
         #     cache_page(604800)
         (SearchResultsView.as_view()), name='search_results'),
    path("latest_movies/",
         # 12 hours
         #     cache_page(60*60*12)
         (LatestMoviesView.as_view()), name="latest_movies"),
    path('<slug:slug>/',
         #     cache_page(604800)
         (MovieDetailView.as_view()), name='movie_detail'),
    path('cast/<int:pk>/',
         #     cache_page(604800)
         (CastMoviesList.as_view()), name='cast_movies_list'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
]
