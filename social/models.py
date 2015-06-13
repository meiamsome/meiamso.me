from django.db import models
from django.utils.html import format_html


class Provider(models.Model):
    """
    This class represents the website or external service that was used to track this data.
    """
    name = models.CharField(max_length=64)
    link = models.URLField()
    join_string = models.CharField(max_length=10, help_text="Used when the Provider is concatenated onto something.")

    def __html__(self):
        return format_html("<a href='{}'>{}</a>", self.link, self.name)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name