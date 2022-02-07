from rest_framework import serializers
from accounts.models import User
from adopt_review.models import Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["nickname"]


class ReviewSerializer(serializers.ModelSerializer):
    nickname = AuthorSerializer(read_only=True)

    class Meta:
        model = Review
        fields = ["number", "nickname", "title", "content", "image"]

