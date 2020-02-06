from django.db import models
from django import forms
from django.utils.safestring import mark_safe
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtailcodeblock.blocks import CodeBlock
from ckeditor.widgets import CKEditorWidget
from djangocodemirror.widgets import CodeMirrorAdminWidget


class RawHTMLCkBlock(blocks.RawHTMLBlock):

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, validators=(), **kwargs):
        super().__init__(required, help_text, max_length, min_length, validators, **kwargs)
        self.field.widget = CodeMirrorAdminWidget(config_name='django')


# Create your models here.
class OrganizationIndexPage(Page):
    code = models.CharField(max_length=30)
    content1 = RichTextField()
    content2 = StreamField([
        ('demo1', blocks.CharBlock(classname="full title")),
        ('demo2', blocks.RichTextBlock()),
        ('demo3', RawHTMLCkBlock()),
        ('demo4', CodeBlock(label='code')),
    ])
    # parent_page_types = []
    parent_page_types = ["home.HomePage"]
    content_panels = Page.content_panels + [
        FieldPanel('code'),
        FieldPanel('content1'),
        StreamFieldPanel('content2'),
    ]
