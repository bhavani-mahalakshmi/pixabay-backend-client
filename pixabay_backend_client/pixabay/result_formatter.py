import math
from config import NO_OF_IMAGES_PER_PAGE

def format_images_list(data):
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
    return result

def format_image_detail(image):
    image_detail = {
        "user": {
            "name": image.get("user"),
            "profile_image": image.get("userImageURL"),
            "id": image.get("id")
        },
        "tags": image.get("tags"),
        "url": image.get("largeImageURL")
    }
    return image_detail