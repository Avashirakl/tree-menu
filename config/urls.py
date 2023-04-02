from django.contrib import admin
from django.urls import path\

from menu.views import main_page, child_page, grandchild_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', main_page, name='main_page'),
    path('child_page/', child_page, name='child_page'),
    path('grandchild_page/', grandchild_page, name='grandchild_page'),
]
