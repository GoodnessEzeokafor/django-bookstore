from django.test import TestCase

# Create your tests here.


class TestPage(TestCase):
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")
        # self.assertContains(response,"Hello, world!")
    
    def test_about_page(self):
        response = self.client.get("/about-us")
        self.assertEqual(response.status_code, 200)
        # self.assertTemplateUsed(response, "about.html")
        # self.assertContains(response, "BookTime is a company that sells books online.")

    def test_contact_us_page_works(self):
        pass