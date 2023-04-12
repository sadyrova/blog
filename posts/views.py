from django.shortcuts import render
from posts.models import Post

# Create your views here.

"""MVC - Model View Controller"""



def main_page_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/index.html')

def post_view(request):
    if request.method == 'GET':
        posts = Post.objects.all()

        context = {
            'posts':posts
        }

        return render(request, 'posts/posts.html', context=context)
