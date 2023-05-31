import os, math, requests
from django.http import JsonResponse, HttpResponseServerError, HttpResponseBadRequest

from pixabay.config import NO_OF_IMAGES_PER_PAGE, PIXABAY_BASE_URL

PIXABAY_API_KEY = os.getenv("PIXABAY_API_KEY", "test")

def image_list(request):
    search_query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    
    url = f"{PIXABAY_BASE_URL}?key={PIXABAY_API_KEY}&q={search_query}&page={page}&per_page={NO_OF_IMAGES_PER_PAGE}"
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponseServerError("An error occurred while fetching images list.")
    
    data = response.json()
    if 'hits' in data:
        images = data.get('hits')
    else:
        images = []
    
    result = {}
    total_pages = math.ceil(data.get('total') / NO_OF_IMAGES_PER_PAGE)
    res_images = []
    for img in images:
        res_images.append({
            "id": img.get("id"),
            "preview_url": img.get("previewURL")
        })
    result = {
        "total_pages": total_pages,
        "images": res_images
    }
    return JsonResponse(result)

def image_detail(request, image_id):
    # Validate image ID
    if not image_id:
        return HttpResponseBadRequest("Image ID is required.")
    
    url = f"{PIXABAY_BASE_URL}?key={PIXABAY_API_KEY}&id={image_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponseServerError("An error occurred while fetching image details.")
    
    data = response.json()
    if 'hits' in data and len(data['hits']) > 0:
        image = data['hits'][0]
    else:
        return HttpResponseBadRequest("Image with ID not found.")
    
    image_details = {
        "user": {
            "name": image.get("user"),
            "profile_image": image.get("userImageURL"),
            "id": image.get("id")
        },
        "tags": image.get("tags"),
        "url": image.get("imageURL")
    }
    
    return JsonResponse(image_details)