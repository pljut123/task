from django import template

from post.models import Follows

register = template.Library()

@register.simple_tag(name='foll')
def get_foll(user, post):
    author = post.author
    try:
        foll = Follows.objects.get(user=user)
        if author in foll.follows.all():
            return True
        else:
            return False
    except Follows.DoesNotExist:
        return False

