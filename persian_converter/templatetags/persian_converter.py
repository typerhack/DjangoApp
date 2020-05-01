from django import template
import persian
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter()
@stringfilter
def convert_to_persian(value):
    return persian.convert_en_numbers(value)
