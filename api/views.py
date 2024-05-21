from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from .models import Todo, Tag
from .serializers import TodoSerializer, TagSerializer, UserSerializer


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def api_root(request):
    """
    Show the API roots/ULRs that the user can take as the starting point
    """
    return Response(
        {
            "todos": reverse("todos", request=request),
            "tags": reverse("tags", request=request),
            "user": reverse("user-detail", request=request),
        }
    )


class TodoListCreateView(generics.ListCreateAPIView):
    """
    List all Todo instances the user created and associated Tags instances, or create a new Todo instance

    Authentication required.
    """

    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, and Delete a specific Todo instance that the user own.
    also show their related Tags instances associated with the Todo instance

    Authentication required.
    """

    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(
            owner=self.request.user
        )  # filter objects that are related to the owner


class TagListCreateView(generics.ListCreateAPIView):
    """
    List all Tag instances that the user created, or create a new Tag instance

    Authentication required.
    """

    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, Update, and Delete a specific Tag instance that the user own.

    Authentication required.
    """

    serializer_class = TagSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Tag.objects.filter(owner=self.request.user)


class UserDetailView(APIView):
    """
    Retrieve User instance details and related data as hyperlinked relationship.

    Authentication required.
    """

    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request):
        serializer = self.serializer_class(
            instance=request.user, context={"request": request}
        )
        return Response(serializer.data)

    # queryset = User.objects.all()

    # def get_queryset(self):
    #     return self.queryset.filter(
    #         id=self.request.user.id
    #     )  # prevent users from spying into other user's details LOL
