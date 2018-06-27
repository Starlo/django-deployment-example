from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    This cuts out all values of "arg" from the srting!
    """
    return value.replace(arg,'')

# register.filter('cut',cut)
