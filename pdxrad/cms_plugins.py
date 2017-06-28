from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Feature

class FeaturePlugin(CMSPluginBase):
    model = Feature
    name = _("Feature Plugin")
    render_template = "plugins/feature.html"
    cache = False

    def render(self, context, instance, placeholder):
        context = super(FeaturePlugin, self).render(context, instance, placeholder)
        return context

plugin_pool.register_plugin(FeaturePlugin)
