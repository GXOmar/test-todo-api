from django.db import models
from django.conf import settings


class Todo(models.Model):
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.CharField(max_length=200, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="todos", on_delete=models.CASCADE
    )
    tag = models.ManyToManyField("Tag", related_name="todos", blank=True)

    class Meta:
        unique_together = ("title", "description")

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="tags", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
