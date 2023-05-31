import math, requests
from django.http import JsonResponse, HttpResponseServerError

from pixabay.config import PIXABAY_API_KEY, NO_OF_IMAGES_PER_PAGE


def image_list(request):
    search_query = request.GET.get('q', '')
    page = int(request.GET.get('page', 1))
    
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&q={search_query}&page={page}&per_page={NO_OF_IMAGES_PER_PAGE}"
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponseServerError("An error occurred while fetching image data.")
    
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
    url = f"https://pixabay.com/api/?key={PIXABAY_API_KEY}&id={image_id}"
    response = requests.get(url)
    if response.status_code != 200:
        return HttpResponseServerError("An error occurred while fetching image details.")
    
    data = response.json()
    image = data['hits'][0]
    
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
