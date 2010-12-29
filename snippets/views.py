# -*- coding: utf8 -*-

from snippets.models import Snippet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def edit( request, object_id ):

	try:
		came_from = request.META['HTTP_REFERER']
	except:
		came_from = False

	context  = 'detail_edit'
	template = 'snippets/snippet_edit.html'

	data = {
		'context' : context,
		'user'    : request.user,
	}

	from snippets.models import Snippet
	from snippets.forms  import SnippetForm

	try:
		snippet = Snippet.objects.get( id = object_id )
	except:
		snippet = None

	form = SnippetForm( request.POST or None, instance = snippet )

	if form.is_valid():
		if not snippet:
			snippet = form.save( commit = False )
		snippet = form.save()
	
	data.update({
		'form' : form,
	})

	if form.is_valid() and came_from and came_from.endswith('/edit'):
		return HttpResponseRedirect( snippet.GetAbsoluteUrl() )

	from django.template import RequestContext
	return render_to_response( template, data, context_instance = RequestContext(request) )


@login_required
def erase( request, object_id ):

	try:
		came_from = request.META['HTTP_REFERER']
	except:
		came_from = False

	try:
		snippet = Snippet.objects.get( id = object_id )
		snippet.delete()
	except:
		pass

	try:
		snippet = Snippet.objects.filter( id__gt = object_id )[0]
	except:
		try:
			snippet = Snippet.objects.filter( id__lt = object_id ).order_by('-id')[0]
		except:
			pass

	# The call came from the list view
	if came_from and came_from.endswith('snippets/'):
		return HttpResponseRedirect( came_from )

	# The call came form the detail view
	return HttpResponseRedirect( snippet.GetAbsoluteUrl() )
