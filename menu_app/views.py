from django.shortcuts import render


def draw_menu(request, menu_item):
    return render(request, 'menu_app/main_menu.html', context={'menu_item': menu_item})