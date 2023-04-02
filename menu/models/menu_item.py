from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class MenuItem(
    models.Model,
):
    """ Модель обьектов меню """
    title = models.CharField(
        _('Название'),
        max_length=128,
    )
    url = models.URLField(
        _('URL-адрес'),
        null=True,
        blank=True,
    )
    named_url = models.CharField(
        _('Название URL'),
        max_length=128,
        null=True,
        blank=True,
    )
    parent = models.ForeignKey(
        'MenuItem',
        on_delete=models.CASCADE,
        related_name='children',
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _('Меню')
        verbose_name_plural = _('Меню')

    def __str__(self):
        return self.title

    def get_url(self):
        if self.named_url:
            return reverse(self.named_url)
        return self.url

    def get_expanded_children(self, current_page):
        expanded_children = []
        for child in self.children.all():
            if child == current_page or (
                    child.parent == current_page.parent) or (
                    child.parent == current_page) or (
                    current_page in child.children.all()):
                expanded_children.append(child)
        return expanded_children
