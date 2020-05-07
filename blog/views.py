from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from django.shortcuts import render, get_object_or_404
from .forms import CommentForm
from .models import Post
from taggit.models import Tag


def post_list(request, tag_slug=None):
    """Display posts"""
    object_list = Post.published.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/table_post.html', {'page': page, 'posts': posts, 'tag': tag})


def specific_post(request, year, month, day, post):
    """Display of a single post"""
    post = get_object_or_404(Post, slug=post, status='published',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    context = {'post': post, 'comments': comments, 'comment_form': comment_form}
    return render(request, 'blog/specific_post.html', context)
