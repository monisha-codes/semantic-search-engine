from django.http import JsonResponse
from django.core.cache import cache
from .models import Document
from .services import get_embedding
from pgvector.django import CosineDistance


def keyword_search(request):

    query = request.GET.get("q")

    if not query:
        return JsonResponse({"error": "Query parameter 'q' is required"}, status=400)

    # -------- Check Cache --------
    cache_key = "keyword:" + query
    cached = cache.get(cache_key)

    if cached:
        return JsonResponse(cached, safe=False)

    # -------- Run Keyword Search --------
    docs = Document.objects.filter(content__icontains=query)[:5]

    results = []

    for d in docs:
        results.append({
            "title": d.title,
            "content": d.content
        })

    # -------- Save Results to Cache --------
    cache.set(cache_key, results, timeout=3600)

    return JsonResponse(results, safe=False)


def semantic_search(request):

    query = request.GET.get("q")

    if not query:
        return JsonResponse({"error": "Query parameter 'q' is required"}, status=400)

    # -------- Check Cache --------
    cache_key = "semantic:" + query
    cached = cache.get(cache_key)

    if cached:
        return JsonResponse(cached, safe=False)

    # -------- Generate Query Embedding --------
    query_embedding = get_embedding(query)

    # -------- Vector Similarity Search --------
    docs = Document.objects.annotate(
        distance=CosineDistance("embedding", query_embedding)
    ).order_by("distance")[:5]

    results = []

    for d in docs:
        results.append({
            "title": d.title,
            "content": d.content,
            "score": float(d.distance)
        })

    # -------- Save Results to Cache --------
    cache.set(cache_key, results, timeout=3600)

    return JsonResponse(results, safe=False)