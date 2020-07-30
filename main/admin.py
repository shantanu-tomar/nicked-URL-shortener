from django.contrib import admin
from .models import URL


class URLAdmin(admin.ModelAdmin):
	list_display = ('id', 'short_description', 'shortened_suffix')


admin.site.register(URL, URLAdmin)
