from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer, UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_root(request):
    return Response(
        {
            "todos": reverse("todos", request=request),
            "tags": reverse("tags", request=request),
            "user": reverse(
                "user-detail", request=request, kwargs={"pk": request.user.id}
            ),
        }
    )


class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(self.request.user, self.request.user.is_authenticated)
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(
            owner=self.request.user
        )  # filter objects that are related to the owner


class TagListCreateView(generics.ListCreateAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(
            id=self.request.user.id
        )  # prevent users from spying into other user's details LOL
