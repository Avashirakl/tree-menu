from django.contrib import admin
from django.urls import path\

from menu.views import page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('main_page/', page, name='main_page'),
]
