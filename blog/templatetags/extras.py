from django import template

register = template.Library()

@register.filter(name='get_val')
def get_val(replydict,item):
    return replydict.get(item)