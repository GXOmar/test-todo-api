from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_root, name="api_root"),
    path("todos/", views.TodoListCreateView.as_view(), name="todos"),
    path(
        "todo/<int:pk>/",
        views.TodoDetailUpdateDeleteView.as_view(),
        name="todo-detail",
    ),
    path("tags/", views.TagListCreateView.as_view(), name="tags"),
    path(
        "tag/<int:pk>/",
        views.TagRetrieveUpdateDestroyView.as_view(),
        name="tag-detail",
    ),
    path("user/<int:pk>/", views.UserDetailView.as_view(), name="user-detail"),
]
