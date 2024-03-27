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
        user = self.request.user
        queryset = Rating.objects.filter(user=user)
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
