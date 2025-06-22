"""
    gets django message w3.css class
    Usage: template filter
"""

from django import template

register = template.Library()


@register.filter(name='msg_w3_class')
def msg_w3_class(message_level):
    """
    gets django message w3.css class name
    """
    w3_css_class = {
        'warning': 'w3-yellow',
        'info': 'w3-blue',
        'success': 'w3-green',
        'error': 'w3-red',
        'debug': 'w3-orange'
    }
    if message_level in w3_css_class:
        return w3_css_class[message_level]
    else:
        return message_level