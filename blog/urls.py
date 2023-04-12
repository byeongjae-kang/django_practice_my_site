from . import views
from django.urls import path


urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("posts/<slug:slug>", views.post_detail, name="post"),
]
