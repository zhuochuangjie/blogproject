from ..models import Post
from django import template
from  ..models import Category

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return  Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()