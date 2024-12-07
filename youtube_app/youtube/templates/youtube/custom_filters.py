from django import template

register = template.Library()

@register.filter
def divided_by(value, divisor):
    try:
        return value / divisor if divisor else None
    except (TypeError, ZeroDivisionError):
        return None
