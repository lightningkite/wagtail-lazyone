from django.db import models
from django.utils.translation import ugettext_lazy as _

from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet

@register_snippet
class TextLinkPane(models.Model):
    RED = '#85090c'
    TRANSPARENT = 'tranparent'
    TAN = '#f0eae4'

    COLOR_CHOICES = (
        (RED, _("Red")),
        (TRANSPARENT, _("Transparent")),
        (TAN, _("Tan")),
    )

    TEXT_COLORS = {
        RED: "#ffffff",
        TRANSPARENT: '#759eaf',
        TAN: '#ff382c',
        'default': '#464d56',
    }

    BUTTON_COLORS = {
        RED: '#ffffff',
        TRANSPARENT: '#464d56',
        TAN: '#464d56',
        'default': '#464d56',
    }

    icon = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.SET_NULL, related_name='+',
        blank=True, null=True)
    background_color = models.CharField(
        max_length=15, choices=COLOR_CHOICES, default=RED)
    text = models.CharField(max_length=255)
    body = models.TextField(
        help_text=_('Will only be used if this is used as a 50% or 75% '
                    'width snippet.'),
        blank=True)
    button_text = models.CharField(
        help_text=_('Leave blank to omit a button.'), max_length=63,
        blank=True)
    link = models.URLField(null=True, blank=True)

    panels = [
        ImageChooserPanel('icon'),
        FieldPanel('background_color'),
        FieldPanel('text'),
        FieldPanel('body'),
        FieldPanel('button_text'),
        FieldPanel('link'),
    ]

    def __str__(self):
        return self.text

    @property
    def text_color(self):
        return TextLinkPane.TEXT_COLORS.get(
            self.background_color, TextLinkPane.TEXT_COLORS['default'])

    @property
    def button_color(self):
        return TextLinkPane.BUTTON_COLORS.get(
            self.background_color, TextLinkPane.BUTTON_COLORS['default'])

    @property
    def button_link(self):
        return self.link or '#'
