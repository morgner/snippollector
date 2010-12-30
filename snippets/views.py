# -*- coding: utf8 -*-

from snippets.models import Snippet
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def edit( request, object_id ):

	# Normally the call comes from a view (list or detail)
	try:
		came_from = request.META['HTTP_REFERER']
	except:
		came_from = False

	context  = 'detail_edit'
	template = 'snippets/snippet_edit.html'

	# These basic data are expected in some templates
	data = {
		'context' : context,
		'user'    : request.user,
	}

	from snippets.models import Snippet
	from snippets.forms  import SnippetForm

	try:
		# If editing an object, the object should exist
		snippet = Snippet.objects.get( id = object_id )
	except:
		# Otherwise we have no object, which is a valid state if adding one
		snippet = None

	# We prepair the form with the snippet ('None' or a valid object)
	form = SnippetForm( request.POST or None, instance = snippet )

	if form.is_valid():
		if not snippet:
			# A new snippet needs a new ID
			snippet = form.save( commit = False )
		snippet = form.save()
	
  # The form is filled correctly and the call came from the edit view
	if form.is_valid() and came_from and came_from.endswith('/edit'):
		# so we return to the snippet details view
		return HttpResponseRedirect( snippet.GetAbsoluteUrl() )

	# It seems to be neccessary to edit the snippet: We add the form to the data
	data.update({
		'form' : form,
	})

  # and we forward the data (and potential error messages) to the edit form
	from django.template import RequestContext
	return render_to_response( template, data, context_instance = RequestContext(request) )


@login_required
def erase( request, object_id ):

	# Normally the call comes from a view (list or detail)
	try:
		came_from = request.META['HTTP_REFERER']
	except:
		came_from = False

	# If the ID is valid, we erase the snippet from the database
	try:
		snippet = Snippet.objects.get( id = object_id )
		snippet.delete()
	except:
		pass

	# The call came from the list view
	if came_from and came_from.endswith('snippets/'):
		return HttpResponseRedirect( came_from )

	# The call came form the detail view
	# Now we search the next snippet to present if returning to detail view
	try:
		# The snippet we expect to show is the next one from the erased one
		snippet = Snippet.objects.filter( id__gt = object_id )[0]
	except:
		try:
			# There was no 'next on' so we search for the last one
			snippet = Snippet.objects.filter( id__lt = object_id ).order_by('-id')[0]
		except:
			# No snippet left - we go to the empty list view
			return HttpResponseRedirect( '/' )

	# We show the 'next best' snippet
	return HttpResponseRedirect( snippet.GetAbsoluteUrl() )
