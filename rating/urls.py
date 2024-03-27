from django.urls import path
from .views import RatingListView, RatingDetailView

urlpatterns = [
    path('ratings/', RatingListView.as_view()),
    path('ratings/<uuid:pk>/', RatingDetailView.as_view()),
]
