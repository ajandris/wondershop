"""
    gets the excerpt with given length from HTML formatted text
    Usage: template filter
"""
import re
from django import template

register = template.Library()

@register.filter(name='get_excerpt')
def get_excerpt(html_text, length):
    """
    Filter get excerpt with given length strips text from HTML
    and returns text with given length
    """
    clean = re.compile('<.*?>')
    cleaned = clean.sub('', html_text)
    cleaned = cleaned.replace("&lt;", "").replace("&gt;", "")
    return cleaned[:length]
