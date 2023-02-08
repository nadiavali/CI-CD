from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm): #take care if using meta then inherit from forms.Modelform
    class Meta:
        model = Feedback
        fields =['email', 'name' , 'message']