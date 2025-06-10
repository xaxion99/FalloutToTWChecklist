from django import template
register = template.Library()


@register.filter
def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    n = int(n)
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


@register.filter
def dict_get(d, key):
    return d.get(key)
