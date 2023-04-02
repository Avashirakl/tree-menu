from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class MenuItem(
    models.Model,
):
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
