# Pixabay Backend Client

This repository contains a backend client that serves as a datasource for a web application, utilizing the Pixabay API to provide image data. The client fulfills the following requirements:

## Features

1. **Image Search Screen**: Users can search for images using a search bar. The screen displays a list of images, which can be clicked for more details. Pagination is implemented for efficient navigation through the image results.

2. **Image Detail Screen**: Upon clicking on an image, users are taken to the image detail screen. This screen presents information about the user who posted the image, along with relevant tags associated with it.

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
