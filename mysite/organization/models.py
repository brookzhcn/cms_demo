from django.db import models
from django import forms
from django.utils.safestring import mark_safe
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtailcodeblock.blocks import CodeBlock
from ckeditor.widgets import CKEditorWidget
from codemirror import CodeMirrorTextarea


class MyCodeMirrorTextarea(CodeMirrorTextarea):
    def render(self, name, value, attrs=None, renderer=None):
        u"""Render CodeMirrorTextarea"""
        if self.js_var_format is not None:
            js_var_bit = 'var %s = ' % (self.js_var_format % name)
        else:
            js_var_bit = ''

        renderer_args = (renderer,)

        output = [super(CodeMirrorTextarea, self).render(
            name, value, attrs, *renderer_args),
            '<script type="text/javascript">%sCodeMirror.fromTextArea(document.getElementById(%s), %s);</script>' %
            (js_var_bit, '"%s"' % name, self.option_json)]
        return mark_safe('\n'.join(output))


codemirror_widget = MyCodeMirrorTextarea(
    mode="html",
    theme="cobalt",
    config={
        'fixedGutter': True
    },
)


class RawHTMLCkBlock(blocks.RawHTMLBlock):

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, validators=(), **kwargs):
        super().__init__(required, help_text, max_length, min_length, validators, **kwargs)
        self.field.widget = codemirror_widget


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
