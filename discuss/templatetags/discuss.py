from django import template

from discuss.util import get_discussion, mark_read

register = template.Library()


@register.inclusion_tag('discuss/discussion.html')
def discussion(obj, user=None):
    """Show thread for object."""

    discussion = get_discussion(obj)

    if user:
        mark_read(discussion, user)

    return {"discussion": get_discussion(obj)}

