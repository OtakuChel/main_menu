from django import template
from django.utils.safestring import mark_safe
from menu_app.models import Menu

register = template.Library()

@register.simple_tag()
def draw_menu(main_menu):
    '''
    Функция обращается к БД для выборки всех записей из модели Menu, после чего
    отбирает ветки выбранного меню.
    main_menu содержит url выбранного раздела меню
    '''
    menu_items = Menu.objects.all().select_related('parent') #все разделы меню
    menu = [] # для хранения главных веток меню
    headers_menu = [i for i in menu_items if not i.parent] #список разделов без родителя
    for it in menu_items:
        if it.url == main_menu:
            menu.append(it)
    while menu[-1].parent:
        menu.append(menu[-1].parent)
    return mark_safe(render_menu([menu[-1], ], menu[::-1], headers_menu))

def render_menu(menu_item, menu, headers_menu):
    '''
    Функция собирает html страничку

    menu_item хранит ссылку на объект, с которого начинается выбранная ветка
    menu хранит ветки выбранного меню
    headers_menu содержит все объекты без атрибута parent
    '''
    menu_html = '<ul>'
    for header in headers_menu:
        if header in menu_item:
            menu_html += render_tree(menu_item, menu)
        else:
            menu_html += '<li>'
            if header.url:
                menu_html += f'<a href="/{header.url}">{header.name}</a>'
            else:
                menu_html += header.name
            menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html

def render_tree(menu_item, menu):

    '''
    Функция возвращает выбранную ветку дерева в формате html кода
    '''
    tree_html = ''
    for item in menu_item:
        tree_html += '<li>'
        if item.url:
            tree_html += f'<a href="/{item.url}">{item.name}</a>'
        else:
            tree_html += item.name
        if item.children and item in menu:
            tree_html += f'<ul>{render_tree(item.children.all(), menu)}</ul>'
        tree_html += '</li>'
    return tree_html