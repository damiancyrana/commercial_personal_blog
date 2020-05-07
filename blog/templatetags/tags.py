from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


@register.inclusion_tag('blog/updates_post.html')
def show_latest_posts(count=3):
    """Show 3 latest posts"""
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=3):
    """Most commented posts"""
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
