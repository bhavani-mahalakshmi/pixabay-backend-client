from django.test import TestCase, Client

class ImageSearchAPITest(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_image_list_endpoint(self):
        response = self.client.get('/image/list/')
        self.assertEqual(response.status_code, 200)
        
    def test_image_list_with_search_query_and_page(self):
        response = self.client.get('/image/list/?q=yellow flower&page=1')
        self.assertEqual(response.status_code, 200)
        
    def test_image_detail_endpoint(self):
        response = self.client.get('/image/2145539/')
        self.assertEqual(response.status_code, 200)

    def test_image_id_not_found_bad_request(self):
        response = self.client.get('/image/')
        self.assertEqual(response.status_code, 400)

    def test_image_detail_not_found_bad_request(self):
        response = self.client.get('/image/1234')
        self.assertEqual(response.status_code, 400)