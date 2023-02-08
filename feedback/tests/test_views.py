from django.test import TestCase
#from feedback.views import 
from http import HTTPStatus


# 200 :success 
# 404: not found
class FeedbackFormTest(TestCase):

    def test_get(self):
        response = self.client.get('/new/')
        #breakpoint()

        self.assertEqual(response.status_code, 200)
        self.assertContains (response, '<h1>Create a new Feedback</h1>')

    def test_post_when_success(self):
        response = self.client.post('/new/', data={'name': 'Nadia', 'message': 'hi Nadia', 'email': 'nadia@example.com'})
        self.assertEqual(response.status_code, 302) #or Httpstatus.found
        self.assertEqual(response['location'], '/') #'/' redirect to home page
    
    def test_template_get(self):
        response = self.client.get('/new/')
        self.assertTemplateUsed(response, 'feedback/new_feedback.html')

    def test_template_post(self):
        response = self.client.post('/new/')
        self.assertTemplateNotUsed(response, 'feedback/new_feedback.html')

        
