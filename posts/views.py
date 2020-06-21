from django.shortcuts import render
from .models import Post
from django.http import JsonResponse

def showPosts(request):
    posts = Post.objects.all()
    context = {}
    context['posts'] = posts

    return render(request, 'posts/index.html', context)

def showPostsApi(request):
    posts = list(Post.objects.values())
    return JsonResponse(posts, safe=False)

def showPostApi(request, id):
    post = list(Post.objects.filter(id=id).values())
    return JsonResponse(post, safe=False)