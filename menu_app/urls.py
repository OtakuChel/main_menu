
from django.urls import path
from .views import draw_menu

urlpatterns = [
    path('<str:menu_item>/', draw_menu, name='draw-menu'),

]