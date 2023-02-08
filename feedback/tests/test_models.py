from django.test import TestCase
from feedback.models import Feedback

class TestFeedbackModel(TestCase):

    def test_feedback_(self):
        feedback = Feedback.objects.create(email='nadia@gmail.com', name='Nadia', message='some message')
        self.assertEqual(str(feedback), 'ID: 1, nadia@gmail.com' )
        self.assertEqual(Feedback.objects.count(), 1)
