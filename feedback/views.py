from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Feedback
from feedback.forms import FeedbackForm
from django.urls import reverse

# Create your views here.

def list_api(request):
    feedback = [{'email': f.email, 'message': f.message} for f in Feedback.objects.all()]
    return JsonResponse({"feedback": feedback})

def list_view(request):
    feedback = Feedback.objects.all()
    return render(request, 'feedback/index.html', {'feedback': feedback})    



def new_feedback(request):
    # do the new feed back by filling the form and post it and create a new feedback and redirect to home page

    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('feedback:list')
    else:
        # the method is get and  by the button of the html file of new_feedback you will get the form and ready to fill it
        form = FeedbackForm()
    return render(request, 'feedback/new_feedback.html', {'form':form}) #form:form is the context variable