from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Post, Comment

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

def archive(request):
    all_posts = Post.objects.all();
    context = {}
    context['posts'] = all_posts
    context['count'] = all_posts.count()
    context['page'] = 'archive'
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

    context['comments'] = post.comment_set.all()

    return render(request, 'blog/post.html', context)

def comment(request):
    
    comment = request.POST.get("comment", "")
    author = request.POST.get("author", "")
    email = request.POST.get("email", "")
    post_title = request.POST.get("post", "")

    post = Post.objects.filter(title = post_title).first()

    user_comment = Comment(author=author, comment=comment, email=email, post=post)
    user_comment.save()

    return HttpResponseRedirect(reverse('blog:post', args=(post.slug,)))
