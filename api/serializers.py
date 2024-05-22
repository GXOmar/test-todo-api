from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Todo, Tag


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get("request", None)
        queryset = super().get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(owner=request.user)


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    # tag = serializers.StringRelatedField(many=True, read_only=True)
    tag = UserFilteredPrimaryKeyRelatedField(queryset=Tag.objects.all(), many=True)

    class Meta:
        model = Todo
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Tag
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = User
        fields = ["id", "username", "todos", "tags"]
