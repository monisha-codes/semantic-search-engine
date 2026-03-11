from django.db import models
from pgvector.django import VectorField


class Document(models.Model):

    title = models.CharField(max_length=500)

    content = models.TextField()

    # Vector embedding for semantic search
    embedding = VectorField(
        dimensions=1536,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title