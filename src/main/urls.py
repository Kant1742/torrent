from django.urls import path, include

from .views import MovieListView, MovieDetailView, AddReview

app_name = 'main'

urlpatterns = [
    path('', MovieListView.as_view(), name='movie_list'),
    path('<slug:slug>/', MovieDetailView.as_view(), name='movie_detail'),
    path("review/<int:pk>/", AddReview.as_view(), name="add_review"),

]
