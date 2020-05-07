from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView


class PostListView(ListView):
    """Displays a posting table"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 6
    template_name = 'blog/table_post.html'


def specific_post(request, year, month, day, post):
    """Display of a single post"""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)
    context = {'post': post}
    return render(request, 'blog/specific_post.html', context)
