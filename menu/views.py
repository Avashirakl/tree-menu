from django.shortcuts import render
from django import template
from menu.models import MenuItem


def page(request):
    return render(request, 'menu/template.html')
