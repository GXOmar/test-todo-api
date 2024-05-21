from django.urls import path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
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
    path("user/", views.UserDetailView.as_view(), name="user-detail"),
]

urlpatterns += [
    # YOUR PATTERNS
    path("schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"
    ),
]
