from django import template
from django.utils.safestring import SafeString
import requests, os, re
from django.conf import settings


register = template.Library()


@register.simple_tag(takes_context=True)
def include_react_dev(context):
    port = getattr(settings, "LOGICORE_DJANGO_REACT_PORT", 3000)
    if not getattr(settings, "FRONTEND_DEV_MODE", False):
        return ''
    return SafeString(
        ' '.join(re.findall(r'<script [^>]+></script>', requests.get(f'http://127.0.0.1:{port}/').text.replace('/static/', '/react-static/')))
    )
