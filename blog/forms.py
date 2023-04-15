from django.forms import ModelForm
from .models import Comment


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]

        label = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your comment",
        }
