from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    pass

class BlogPage(Page):
    pass

class PostPage(Page):
    pass


class BasePage(Page):
    pass

class VideoPage(Page):
    name = models.CharField(max_length=255)
    tag = models.CharField(max_length=255)
    body = models.TextField(max_length=100)
    device = models.TextField(max_length=100)
    post = models.TextField(max_length=100)

    content_panels = Page.content_panels + [
    FieldPanel("name"),
    FieldPanel("post"),
    FieldPanel("body"),
    FieldPanel("device"),
    FieldPanel("tag"),

    ]