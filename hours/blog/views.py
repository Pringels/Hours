from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post

def archive(request):
    all_posts = Post.objects.all();
    context = {}
    context['posts'] = all_posts
    context['count'] = all_posts.count()
    return render(request, 'blog/archive.html', context)


def post(request, slug):
    if slug:
        post = Post.objects.filter(slug = slug).first()
    else:
        post = Post.objects.latest();
    context = {}
    context['title'] = post.title
    context['post_date'] = post.post_date
    context['content'] = post.content
    return render(request, 'blog/post.html', context)
