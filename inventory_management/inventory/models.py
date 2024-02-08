from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class InventoryItem(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nombre'))
    quantity = models.IntegerField(verbose_name=_('Cantidad'))
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, blank=True, null=True, verbose_name=_('Categoría'))
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_('Fecha de creación'))
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_('Usuario'))

    class Meta:
        verbose_name = _('Elemento de inventario')
        verbose_name_plural = _('Elementos de inventario')

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=_('Nombre'))

    class Meta:
        verbose_name = _('Categoría')
        verbose_name_plural = _('Categorías')

    def __str__(self):
        return self.name