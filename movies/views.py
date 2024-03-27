from django.http import JsonResponse
from .api_movies_service import ApiMoviesService
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
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
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_best_assessment(request):
    page = request.GET.get("page", 1)
    api = ApiMoviesService()
    best_assessment = api.listBestRated(page).json()
    return JsonResponse(best_assessment)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_movies_MovieTheater(request):
    page = request.GET.get("page", 1)
    api = ApiMoviesService()
    movies_MovieTheater = api.listMoviesMovieTheater(page).json()
    return JsonResponse(movies_MovieTheater)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def find_movies(request):
    query = request.GET.get("query")
    api = ApiMoviesService()
    result = api.filterMovies(query).json()
    return JsonResponse(result)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def detail_movie(request, id_movie):
    api = ApiMoviesService()
    detail_movie = api.getMovieById(id_movie).json()
    return JsonResponse(detail_movie)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def credits_movie(request, id_movie):
    api = ApiMoviesService()
    credits_movie = api.getCreditsMovie(id_movie).json()
    return JsonResponse(credits_movie)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def providers_movie(request, id_movie):
    api = ApiMoviesService()
    providers_movie = api.getProviders(id_movie).json()
    return JsonResponse(providers_movie)


@api_view(["GET"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def list_genres(request):
    api = ApiMoviesService()
    genres = api.getGenres().json()
    return JsonResponse(genres)
