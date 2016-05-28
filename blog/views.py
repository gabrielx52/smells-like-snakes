from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


def front_page(request):
    post_title = Post.objects.all()
    context = {'Post': post_title}
    return render(request, 'blog/front_page.html', context)


def detail(request, post_id):
    #return HttpResponse('You\'re looking at post {}'.format(post_id))
    posted = Post.objects.get(pk=post_id)
    context = {"post_id": posted}
    return render(request, 'blog/detail.html', context)
