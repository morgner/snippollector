from django import template

register = template.Library()

def paginator(context, adjacent_pages=3):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.

    """
    ap2 = adjacent_pages/2
    pn  = context['page']
    first_page = pn - ap2
    if first_page + adjacent_pages > context['pages']:
        first_page = context['pages'] - adjacent_pages +1
    if first_page < 1:
        first_page = 1
    page_numbers = [n for n in \
                    range(first_page, first_page + adjacent_pages) \
                    if n <= context['pages']]
    return {
        'hits': context['hits'],
        'results_per_page': context['results_per_page'],
        'page': context['page'],
        'pages': context['pages'],
        'page_numbers': page_numbers,
        'next': context['next'],
        'previous': context['previous'],
        'has_next': context['has_next'],
        'has_previous': context['has_previous'],
        'show_first': 1 not in page_numbers,
        'show_last': context['pages'] not in page_numbers,
    }

register.inclusion_tag('paginator.html', takes_context=True)(paginator)
