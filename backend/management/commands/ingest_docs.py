import json
from django.core.management.base import BaseCommand
from search_app.models import Document
from search_app.services import get_embedding


class Command(BaseCommand):

    def handle(self, *args, **kwargs):

        with open("data/documents.json") as f:
            docs = json.load(f)

        for doc in docs:

            embedding = get_embedding(doc["content"])

            Document.objects.create(
                title=doc["title"],
                content=doc["content"],
                embedding=embedding
            )

        print("Documents inserted successfully")