from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    name = models.CharField(max_length=50, blank=False, null=False, verbose_name=_('Name'))
    email = models.EmailField(blank=False, null=False, verbose_name=_('Email'))
    subject = models.CharField(max_length=100, blank=True, verbose_name=_('Subject'))
    message = models.TextField(max_length=500, blank=False, null=False, verbose_name=_('Message'))
    datetime_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"

