from django import template

register = template.Library()

@register.filter
def split(value, arg=','):
    """Vergul bo'yicha ajratadi"""
    if value:
        return [item.strip() for item in value.split(arg)]
    return []

@register.filter
def strip(value):
    """Bo'sh joylarni olib tashlaydi"""
    if value:
        return value.strip()
    return value