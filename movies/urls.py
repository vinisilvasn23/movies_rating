from django.urls import path
from . import views

urlpatterns = [
    path(
        "movies/popular/",
        views.list_popular_movies,
    ),
    path(
        "movies/best-assessment/",
        views.list_best_assessment,
    ),
    path(
        "movies/movie-theater/",
        views.list_movies_MovieTheater,
    ),
    path("movies/busca/", views.find_movies),
    path("movies/<int:id_movie>/", views.detail_movie),
    path("movies/<int:id_movie>/credits/", views.credits_movie),
    path(
        "movies/<int:id_movie>/providers/",
        views.providers_movie,
    ),
    path("genres/", views.list_genres),
    path("movie/<int:id_movie>/translations/", views.translation_movie),
]
