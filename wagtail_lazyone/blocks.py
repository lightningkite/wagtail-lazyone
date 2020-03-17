from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import (
    CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock, URLBlock, StaticBlock, URLBlock
)

from .models import TextLinkPane


class FourWaySplitBlock(StructBlock):
    WHITE = '#ffffff'
    TAN = '#f0eaea4'
    TRANSPARENT = 'transparent'

    COLOR_CHOICES = (
        (WHITE, 'White'),
        (TAN, 'Tan'),
        (TRANSPARENT, 'Transparent'),
    )

    IMAGE_IMAGE_IMAGE_IMAGE = 'i-i-i-i'
    IMAGE_IMAGE_IMAGE_SNIPPET = 'i-i-i-s'
    IMAGE_IMAGE_SNIPPET_IMAGE = 'i-i-s-i'
    IMAGE_SNIPPET_IMAGE_IMAGE = 'i-s-i-i'
    SNIPPET_IMAGE_IMAGE_IMAGE = 's-i-i-i'
    IMAGE_IMAGE_SNIPPET_SNIPPET = 'i-i-s-s'
    IMAGE_SNIPPET_IMAGE_SNIPPET = 'i-s-i-s'
    IMAGE_SNIPPET_SNIPPET_IMAGE = 'i-s-s-i'
    SNIPPET_IMAGE_IMAGE_SNIPPET = 's-i-i-s'
    SNIPPET_IMAGE_SNIPPET_IMAGE = 's-i-s-i'
    SNIPPET_SNIPPET_IMAGE_IMAGE = 's-s-i-i'
    IMAGE_SNIPPET_SNIPPET_SNIPPET = 'i-s-s-s'
    SNIPPET_IMAGE_SNIPPET_SNIPPET = 's-i-s-s'
    SNIPPET_SNIPPET_IMAGE_SNIPPET = 's-s-i-s'
    SNIPPET_SNIPPET_SNIPPET_IMAGE = 's-s-s-i'
    SNIPPET_SNIPPET_SNIPPET_SNIPPET = 's-s-s-s'

    split_type = ChoiceBlock(
        choices=[
            (IMAGE_IMAGE_IMAGE_IMAGE, 'image|image|image|image'),
            (IMAGE_IMAGE_IMAGE_SNIPPET, 'image|image|image|snippet'),
            (IMAGE_IMAGE_SNIPPET_IMAGE, 'image|image|snippet|image'),
            (IMAGE_SNIPPET_IMAGE_IMAGE, 'image|snippet|image|image'),
            (SNIPPET_IMAGE_IMAGE_IMAGE, 'snippet|image|image|image'),
            (IMAGE_IMAGE_SNIPPET_SNIPPET, 'image|image|snippet|snippet'),
            (IMAGE_SNIPPET_IMAGE_SNIPPET, 'image|snippet|image|snippet'),
            (IMAGE_SNIPPET_SNIPPET_IMAGE, 'image|snippet|snippet|image'),
            (SNIPPET_IMAGE_IMAGE_SNIPPET, 'snippet|image|image|snippet'),
            (SNIPPET_IMAGE_SNIPPET_IMAGE, 'snippet|image|snippet|image'),
            (SNIPPET_SNIPPET_IMAGE_IMAGE, 'snippet|snippet|image|image'),
            (IMAGE_SNIPPET_SNIPPET_SNIPPET, 'image|snippet|snippet|snippet'),
            (SNIPPET_IMAGE_SNIPPET_SNIPPET, 'snippet|image|snippet|snippet'),
            (SNIPPET_SNIPPET_IMAGE_SNIPPET, 'snippet|snippet|image|snippet'),
            (SNIPPET_SNIPPET_SNIPPET_IMAGE, 'snippet|snippet|snippet|image'),
            (SNIPPET_SNIPPET_SNIPPET_SNIPPET, 'snippet|snippet|snippet|snippet'),
        ]    
    )

    first_image = ImageChooserBlock()
    second_image = ImageChooserBlock()
    third_image = ImageChooserBlock()
    fourth_image = ImageChooserBlock()
    first_url = URLBlock(required=False)
    second_url = URLBlock(required=False)
    third_url = URLBlock(required=False)
    fourth_url = URLBlock(required=False)

    first_snippet = SnippetChooserBlock(TextLinkPane, required=False)
    second_snippet = SnippetChooserBlock(TextLinkPane, required=False)
    third_snippet = SnippetChooserBlock(TextLinkPane, required=False)
    fourth_snippet = SnippetChooserBlock(TextLinkPane, required=False)

    background_color = ChoiceBlock(choices=COLOR_CHOICES, default=WHITE)

    class Meta:
        icon = 'list-ul'
        template = 'wagtail_lazyone/blocks/split_block_4.html'
        form_template = 'wagtail_lazyone/admin/blocks/split_block_4.html'

    def sections(self):
        return dir(self)

