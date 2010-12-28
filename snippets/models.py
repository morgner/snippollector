# -*- coding: utf8 -*-

from django.db import models
from settings import SNIPPET_APPL

class Snippet(models.Model):
	name = models.CharField(max_length=100)
	code = models.TextField()
	lang = models.ForeignKey('Language')
	author = models.CharField(max_length=72)
	pub_date = models.DateTimeField('date published', auto_now_add = True)
	
	def __unicode__(self):
		return self.name
	
	def GetAbsoluteUrl(self):
		return '/%s/%s' % ( SNIPPET_APPL, self.id )

class Language(models.Model):
	name = models.CharField(max_length=40)
	version = models.FloatField()
	
	def __unicode__(self):
		description = '%s (%s)' % ( self.name, self.version )
		return description
	
	def GetLowercaseName(self):
		return self.name.lower()
	
