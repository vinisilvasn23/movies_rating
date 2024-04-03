from django.http import JsonResponse
from .api_movies_service import ApiMoviesService
from rest_framework.authentication import TokenAuthentication
from .permission import IsUserPermission
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def list_popular_movies(request):
    page = request.GET.get("page", 1)
    api = ApiMoviesService()
    popular_movies = api.listMoviesPopular(page).json()
    return JsonResponse(popular_movies)


@api_view(["GET"])
@permission_classes([IsUserPermission])
def list_best_assessment(request):
    page = request.GET.get("page", 1)
    api = ApiMoviesService()
    best_assessment = api.listBestRated(page).json()
    return JsonResponse(best_assessment)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def list_movies_MovieTheater(request):
    page = request.GET.get("page", 1)
    api = ApiMoviesService()
    movies_MovieTheater = api.listMoviesMovieTheater(page).json()
    return JsonResponse(movies_MovieTheater)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def find_movies(request):
    query = request.GET.get("query")
    api = ApiMoviesService()
    result = api.filterMovies(query).json()
    return JsonResponse(result)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def detail_movie(request, id_movie):
    api = ApiMoviesService()
    detail_movie = api.getMovieById(id_movie).json()
    return JsonResponse(detail_movie)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def credits_movie(request, id_movie):
    api = ApiMoviesService()
    credits_movie = api.getCreditsMovie(id_movie).json()
    return JsonResponse(credits_movie)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def providers_movie(request, id_movie):
    api = ApiMoviesService()
    providers_movie = api.getProviders(id_movie).json()
    return JsonResponse(providers_movie)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def list_genres(request):
    api = ApiMoviesService()
    genres = api.getGenres().json()
    return JsonResponse(genres)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
def translation_movie(request, id_movie):
    api = ApiMoviesService()
    translation_movie = api.translation(id_movie).json()
    return JsonResponse(translation_movie)
