from django.shortcuts import render
from django import template
from menu.models import MenuItem


def main_page(request):
    return render(request, 'menu/template.html')


def child_page(request):
    return render(request, 'menu/child.html')


def grandchild_page(request):
    return render(request, 'menu/grandchild.html')
