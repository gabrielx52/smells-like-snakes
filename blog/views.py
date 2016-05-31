from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Post


def front_page(request):
    """ Main page """
    published = Post.objects.exclude(date_published__exact=None)
    recent_posts = published.order_by('-date_published')[:5]
    post_title = Post.objects.all()
    context = {'post': post_title, 'recent_posts': recent_posts}
    return render(request, 'blog/front_page.html', context)


def detail_view(request, post_id):
    """ Detailed post view """
    published = Post.objects.exclude(date_published__exact=None)
    recent_posts = published.order_by('-date_published')[:5]
    try:
        post = published.get(pk=post_id)
    except post.DoesNotExist:
        raise Http404
    context = {'post': post, 'recent_posts': recent_posts}
    return render(request, 'blog/detail.html', context)


def about_view(request):
    """ About page """
    published = Post.objects.exclude(date_published__exact=None)
    recent_posts = published.order_by('-date_published')[:5]
    return render(request, 'blog/about.html', {'recent_posts': recent_posts})
