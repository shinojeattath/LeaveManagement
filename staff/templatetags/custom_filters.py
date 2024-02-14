# custom_filters.py

from django import template

register = template.Library()

@register.filter
def custom_range(start, end):
    return range(1, 3)

@register.filter
def increment(value):
    return value + 1
