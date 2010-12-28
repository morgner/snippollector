# -*- coding: utf8 -*-

from django import forms
from snippets.models import *

class SnippetForm(forms.ModelForm):

	class Meta:
		model = Snippet
		fields = ( 'name', 'code', 'lang', 'author' )

	name   = forms.CharField ( widget = forms.TextInput(attrs={'size': 64,             'class': 'name',   }), label = u'Name' )
	code   = forms.CharField ( widget = forms.Textarea (attrs={'cols': 64, 'rows': 16, 'class': 'code',   }), label = u'Code' )
#	lang   = forms.ForeignKey( Language, verbose_name = 'Language')
	author = forms.CharField ( widget = forms.TextInput(attrs={'size': 42,             'class': 'author', }), label = u'Author' )
#	pub_date = forms.DateTimeField( ???, )
