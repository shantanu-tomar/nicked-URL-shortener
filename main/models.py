from django.db import models
from django.template.defaultfilters import truncatechars


class URL(models.Model):
    original_url = models.URLField(max_length=2000)
    shortened_suffix = models.CharField(max_length=25 , unique=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name_plural='URLs'


    def save(self, *args, **kwargs):
        self.shortened_suffix = '.' + self.shortened_suffix
        super().save(*args, **kwargs)

    
    @property
    def short_description(self):
        return truncatechars(self.original_url, 35)