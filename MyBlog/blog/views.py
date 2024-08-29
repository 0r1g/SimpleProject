from django.shortcuts import render
from .models import Post


# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'post_list': posts
    }
    return render(request, 'blog/post_list.html', context)
