from django.shortcuts import render
from .models import Post, Author


# Create your views here.


def index(request):
    posts = Post.objects.all()

    context = {
        'post_list': posts
    }
    return render(request, 'blog/post_list.html', context)


def get_post(request, post_id):
    post = Post.objects.get(id=post_id)

    context = {
        'post': post
    }
    return render(request, 'blog/post.html', context)


def get_posts_by_author(request, author_id):

    context = {
        'author': Author.objects.get(id=author_id),
        'posts': Post.objects.filter(author_id=author_id)
    }
    return render(request, 'blog/posts_by_author.html', context)
