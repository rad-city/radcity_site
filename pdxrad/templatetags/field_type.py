from django import template
register = template.Library()

@register.filter(name='field_type')
def input_type(field):
    return field.field.widget.__class__.__name__
