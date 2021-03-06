from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def lower_bnd(value):
    return mark_safe("-&#8734;") if value == "None" else value

@register.filter
@stringfilter
def upper_bnd(value):
    return mark_safe("+&#8734;") if value == "None" else value

@register.filter
@stringfilter
def none_prmin(value):
    return "1e-3" if value == "None" else value

@register.filter
@stringfilter
def none_prmax(value):
    return "1e+3" if value == "None" else value

@register.filter
@stringfilter
def none_null(value):
    return "null" if value == "None" else value