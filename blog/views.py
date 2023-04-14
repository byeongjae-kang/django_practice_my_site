from django.shortcuts import get_object_or_404, render
from .models import Post


def get_date(post):
    return post["date"]


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {"posts": latest_posts})


def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/posts.html", {"posts": all_posts})


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {"post": identified_post})
