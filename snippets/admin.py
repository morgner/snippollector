# -*- coding: utf8 -*-

from snippets.models import Snippet
from snippets.models import Language
from django.contrib import admin

class SnippetAdmin(admin.ModelAdmin):
	list_display = ('name', 'lang', 'author')

admin.site.register(Snippet, SnippetAdmin)
admin.site.register(Language)
