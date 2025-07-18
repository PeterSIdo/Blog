# Blog/myblog/views.py
from django.shortcuts import render
from .models import Post  # Ensure you have a Post model defined in models.py
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'myblog/post-list.html', {'posts': posts})