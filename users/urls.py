from django.urls import path
from .views import UserListView, UserDetailView
from rest_framework_simplejwt.views import TokenRefreshView
from .serializers import CustomTokenObtainPairView

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('users/<uuid:pk>/', UserDetailView.as_view()),
    path("login/", CustomTokenObtainPairView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view()),
]
