# Pixabay Backend Client

This repository contains a backend client that serves as a datasource for a web application, utilizing the Pixabay API to provide image data. The client assumes that the default number of image results returned as 10. This value is configurable and is located in the `pixabay/config.py` file as `NO_OF_IMAGES_PER_PAGE`. The client fulfills the following requirements:

1. **Image Search Screen**: Users can search for images using a search bar. The screen displays a list of images, which can be clicked for more details. Pagination is implemented for efficient navigation through the image results.

2. **Image Detail Screen**: Upon clicking on an image, users are taken to the image detail screen. This screen presents information about the user who posted the image, along with relevant tags associated with it.

## API
1. List images: `/image/list`

This endpoint will list the images with optional conditions.

   a. `/image/list` will list the first 10 images(page 1) on pixabay without any condition

   b. `/image/list?q=<search query>` will return the first 10 images(page 1) for the given search query

   c. `/image/list?page=12` will return the 12th page from the pixabay data source without any condition

   d. `/image/list?q=red flower&page=12` will return the 12th page from the pixabay data source for images that match the `red flower` search query

2. Image detail: `/image/<image_id>`

This endpoint will return the details of the image with the given ID. If the ID is not passed or invalid, the api will throw a Bad request error with the corresponsing error message. 


## Installation

To set up the Pixabay backend client, follow these steps:

1. Clone this repository to your local machine.

2. Install the requirements using:
   
   ```shell
   pip install -r requirements.txt
   ```


3. Obtain an API key from Pixabay by following the [Pixabay API documentation](https://pixabay.com/api/docs/).

4. Set your Pixabay API key as an environment variable in your local development environment:
   
   ```shell
   export PIXABAY_API_KEY=<your_api_key>
   ```
## Usage
   
   ```shell
   python manage.py runserver
   ```

## Running Tests

To run the tests and ensure that the APIs are working correctly, execute the following command:
   
   ```shell
   python manage.py test
   ```
