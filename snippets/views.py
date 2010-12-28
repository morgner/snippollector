# -*- coding: utf8 -*-

from snippets.models import Snippet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response

def edit( request, object_id ):

	came_from = request.META['HTTP_REFERER']
	print 'Came From %s' % ( came_from, )
	
	context  = 'detail_edit'
	template = 'snippets/snippet_edit.html'
	
	data = {
		'context' : context,
		'user'    : request.user,
	}
	
	from snippets.models import Snippet
	from snippets.forms  import SnippetForm

	snippet = Snippet.objects.get( id = object_id )
	form    = SnippetForm( request.POST or None, instance = snippet )

	if form.is_valid():
		if not snippet:
			snippet = form.save( commit = False )
		snippet = form.save()
	
	data.update({
		'form'   : form,
	})

	if came_from and came_from.endswith('/edit'):
		return HttpResponseRedirect( snippet.GetAbsoluteUrl() )

	from django.template import RequestContext
	return render_to_response( template, data, context_instance = RequestContext(request) )
