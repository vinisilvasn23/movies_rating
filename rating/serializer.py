from rest_framework import serializers
from .models import Rating
from users.serializers import UserSerializer


class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Rating
        fields = "__all__"

    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user_id"] = user.id
        rating = Rating.objects.create(**validated_data)
        return rating


class RatingDetailSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    class Meta:
        model = Rating
        fields = ["id", "user", "movie_id", "rating"]
        read_only_fields = ["id", "user"]
