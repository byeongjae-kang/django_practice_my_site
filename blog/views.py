from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import DetailView, ListView, View
from .forms import CommentForm
from .models import Post


class IndexView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


class Posts(ListView):
    template_name = "blog/posts.html"
    model = Post
    ordering = ["-date"]
    context_object_name = "posts"


class PostDetail(View):
    template_name = "blog/post_detail.html"
    model = Post

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comments = post.comments.all().order_by("-id")
        is_saved_for_later = post.id in request.session.get("stored_posts", {})
        form = CommentForm()
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "form": form,
                "post_tags": post.tags.all(),
                "comments": comments,
                "is_saved_for_later": is_saved_for_later,
            },
        )

    def post(self, request, slug):
        form = CommentForm(request.POST)
        post = Post.objects.get(slug=slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return HttpResponseRedirect(reverse("post", args=[slug]))

        comments = post.comments.all().order_by("-id")
        is_saved_for_later = post.id in request.session.get("stored_posts")
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "form": form,
                "post_tags": post.tags.all(),
                "comments": comments,
                "is_saved_for_later": is_saved_for_later,
            },
        )


class ReadLaterView(View):
    def get(self, request):
        stored_posts = request.session.get("stored_posts")

        context = {}

        if stored_posts is None or len(stored_posts) == 0:
            context["posts"] = []
            context["has_posts"] = False
        else:
            posts = Post.objects.filter(id__in=stored_posts)
            context["posts"] = posts
            context["has_posts"] = True

        return render(request, "blog/stored_posts.html", context)

    def post(self, request):
        stored_posts = request.session.get("stored_posts")

        if stored_posts is None:
            stored_posts = []

        post_id = int(request.POST["post_id"])
        if post_id not in stored_posts:
            stored_posts.append(post_id)
        else:
            stored_posts.remove(post_id)

        request.session["stored_posts"] = stored_posts
        return HttpResponseRedirect("/")
