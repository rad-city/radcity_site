from cms.models.pluginmodel import CMSPlugin, Placeholder
from cms.models.fields import PlaceholderField
from django.db import models

class Feature(CMSPlugin):
    title = models.CharField( max_length=64, default='Feature Title')
    blurb = models.CharField(max_length=256, default='Just a short blurb here.')
    img = models.CharField(max_length=256)
    link = models.CharField(max_length=256)
