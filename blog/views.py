from django.shortcuts import render, get_object_or_404
from .models import Post


def table_post(request):
    """Displays a posting table"""
    posts = Post.published.all()
    context = {'posts': posts}
    return render(request, 'blog/table_post.html', context)


def specific_post(request, year, month, day, post):
    """Display of a single post"""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post': post}
    return render(request, 'blog/specific_post.html', context)
