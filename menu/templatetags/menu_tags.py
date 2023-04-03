from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html', takes_context=True)
def draw_menu(context, title):
    request = context['request']
    all_items = MenuItem.objects.all().select_related('parent')
    menu_items = all_items.filter(title=title)
    current_page = all_items.get(named_url=request.resolver_match.url_name)
    return {'menu_items': menu_items, 'current_page': current_page, }


@register.filter
def get_expanded_children(item, current_page):
    return item.get_expanded_children(current_page)
