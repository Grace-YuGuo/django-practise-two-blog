from django.shortcuts import render
# from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
# def func_one(request):
#     return HttpResponse('Hello,Blog')
class PostList(generic.ListView):
    # model= Post
    queryset = Post.objects.all()
    template_name = 'post_list.html'
