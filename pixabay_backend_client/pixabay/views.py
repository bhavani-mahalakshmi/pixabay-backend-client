import requests
from django.http import JsonResponse

from pixabay.config import PIXABAY_API_KEY, NO_OF_IMAGES_PER_PAGE


def image_list(request):
    search_query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={search_query}&page={page}&per_page={NO_OF_IMAGES_PER_PAGE}"
    response = requests.get(url)
    data = response.json()
    if 'hits' in data:
        images = data['hits']
    else:
        images = []
    
    return JsonResponse(images)