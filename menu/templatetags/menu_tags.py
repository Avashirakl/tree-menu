from django import template
from menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/menu.html')
def draw_menu(title):
    menu_items = MenuItem.objects.filter(title=title)
    return {'menu_items': menu_items}
