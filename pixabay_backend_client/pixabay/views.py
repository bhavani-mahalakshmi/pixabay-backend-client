import requests
from django.http import JsonResponse, HttpResponseServerError, HttpResponseBadRequest

from pixabay.config import NO_OF_IMAGES_PER_PAGE, PIXABAY_BASE_URL
from pixabay.result_formatter import format_image_detail, format_images_list
from django.conf import settings

def image_list(request):
    try:
        search_query = request.GET.get('q', '')
        page = int(request.GET.get('page', 1))
        
        url = f"{PIXABAY_BASE_URL}?key={settings.PIXABAY_API_KEY}&q={search_query}&page={page}&per_page={NO_OF_IMAGES_PER_PAGE}"
        response = requests.get(url)
        if response.status_code != 200:
            return HttpResponseServerError("An error occurred while fetching images list.")
        
        data = response.json()
        result = format_images_list(data)
        return JsonResponse(result)
    except Exception as e:
        print(e)
        return HttpResponseServerError("An error occurred while fetching images list.")
    
def image_detail(request, image_id):
    try:
        # Validate image ID
        if not image_id:
            return HttpResponseBadRequest("Image ID is required.")
        
        url = f"{PIXABAY_BASE_URL}?key={settings.PIXABAY_API_KEY}&id={image_id}"
        response = requests.get(url)
        if response.status_code != 200:
            return HttpResponseServerError("An error occurred while fetching image details.")
        
        data = response.json()
        if 'hits' in data and len(data['hits']) > 0:
            image = data['hits'][0]
        else:
            return HttpResponseBadRequest("Image with ID not found.")
        
        image_detail = format_image_detail(image)
        
        return JsonResponse(image_detail)
    except Exception as e:
        print(e)
        return HttpResponseServerError("An error occurred while fetching image details.")
    