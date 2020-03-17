from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


REVERSE = {
    'i': 'image',
    's': 'snippet',
}

REVERSE_N = [
    'first',
    'second',
    'third',
    'fourth'
]


@register.filter
def four_way_sections(struct_value):
    for i, t in enumerate(struct_value.get('split_type').split('-')):
        yield (
            struct_value.get('{}_{}'.format(REVERSE_N[i], REVERSE[t])),
            struct_value.get('{}_url'.format(REVERSE_N[i])),
            REVERSE[t]
        )
