from django.urls import path, include

from .views import (MovieListView, MovieDetailView, AddReview,
                    SearchResultsView, LatestMoviesView)

app_name = 'main'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path("latest_movies/", LatestMoviesView.as_view(), name="latest_movies"),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),
]
