from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from django.contrib import messages
from .models import About
from django.shortcuts import render,get_object_or_404
from .forms import CollaborateRequestForm

# Create your views here.
def about(request):
    """
    Display an individual : model:`about.About`.
    **Context**

    ``post``
        An instance of : model:`about.About`.

    **Template:**
    :template:`about/About.html`
    """
    about = About.objects.all().order_by('-created_on').first()
    # Handle the POST request from the comment form
    if request.method == "POST":
         collaborator_form = CollaborateRequestForm(data=request.POST)
         print(collaborator_form)
         if collaborator_form.is_valid():
            collaborate = collaborator_form.save(commit=False)
            collaborate.read=False
            collaborate.save()
            messages.add_message(request,messages.SUCCESS,'Collaboration request received! I endeavour to respond within 2 working days.')

    collaborator_form = CollaborateRequestForm()
    return render(request,"about/about.html",{"about":about,
    'collaborator_request_form':collaborator_form,}
    )