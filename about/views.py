from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from django.shortcuts import render,get_object_or_404
from .models import About
from .forms import CollaborateRequestForm

# Create your views here.
def about(request):
    """
    Renders the most recent information on the website author and allows user collaboraton requests.
    Display an individual : model:`about.About`.
    **Context**
    ``about``
        The most recent instance of :model: `about.About`
    ``collaborate_form`
        An instance of :form:`about.CollaborateForm`.
    **Template:**
    :template:`about/About.html`
    """
    about = About.objects.all().order_by('-created_on').first()
    # Handle the POST request from the comment form
    if request.method == "POST":
         collaborator_form = CollaborateRequestForm(data=request.POST)
         if collaborator_form.is_valid():
            collaborate = collaborator_form.save(commit=False)
            collaborate.read=False
            collaborate.save()
            messages.add_message(request,messages.SUCCESS,'Collaboration request received! I endeavour to respond within 2 working days.')

    collaborator_form = CollaborateRequestForm()
    return render(request,"about/about.html",{"about":about,
    'collaborator_request_form':collaborator_form,}
    )