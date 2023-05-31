from django.test import TestCase, Client, override_settings

@override_settings(PIXABAY_API_KEY='36900313-f8e256b3a18ea6d023f20e116')
class ImageSearchAPITest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_image_list_endpoint(self):
        response = self.client.get('/image/list')
        self.assertEqual(response.status_code, 200, response.content.decode())

    def test_image_list_with_search_query_and_page(self):
        response = self.client.get('/image/list?q=yellow flower&page=1')
        self.assertEqual(response.status_code, 200, response.content.decode())

    def test_image_detail_endpoint(self):
        response = self.client.get('/image/2145539')
        self.assertEqual(response.status_code, 200, response.content.decode())

    def test_image_id_not_found_bad_request(self):
        response = self.client.get('/image/000')
        self.assertEqual(response.status_code, 400, response.content.decode())