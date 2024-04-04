from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Rating
from .serializer import RatingSerializer, RatingDetailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .permission import IsRatingUser
from rest_framework import status
from rest_framework.response import Response


class RatingListView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

    def get_queryset(self):
        queryset = Rating.objects.all()
        movie_id = self.request.query_params.get("movie_id", None)
        if movie_id is not None:
            queryset = queryset.filter(movie_id=movie_id)
        return queryset

    def perform_create(self, serializer):
        movie_id = serializer.validated_data.get("movie_id")
        existing_rating = Rating.objects.filter(
            user=self.request.user, movie_id=movie_id
        ).first()
        if existing_rating:
            return Response(
                {
                    "detail": "A rating for this movie already exists for the current user."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer.save(user=self.request.user)


class RatingDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsRatingUser]
    queryset = Rating.objects.all()
    serializer_class = RatingDetailSerializer
