from . import views
from django.urls import path


urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("posts", views.Posts.as_view(), name="posts"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    path("posts/<slug:slug>", views.PostDetail.as_view(), name="post"),
]
