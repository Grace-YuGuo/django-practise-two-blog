from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import About
from django.shortcuts import render,get_object_or_404

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

    return render(request,"about/about.html",{"about":about,},
    )