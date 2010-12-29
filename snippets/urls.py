# -*- coding: utf8 -*-

from django.conf.urls.defaults import *

#from django.contrib.auth.decorators import login_required
from django.views.generic.list_detail import object_list, object_detail

from snippets.conf   import settings
from snippets.models import *


snippet_dict = {
  'queryset'    : Snippet.objects.all(),
  'paginate_by' : settings.PAGINATE_BY,
}

snippet_detail = {
  'queryset'    : Snippet.objects.all(),
}

urlpatterns = patterns('django.views.generic.list_detail',
  url(r'^$',                    'object_list',   snippet_dict,   name='snippet_list'),
  url(r'^(?P<object_id>\d+)/$', 'object_detail', snippet_detail, name='snippet_detail'),
  )

urlpatterns += patterns('django.views.generic.simple',
  url(r'^new$', 'redirect_to', { 'url': '0/edit' }, name='snippet_new'),
  )

urlpatterns += patterns('snippets.views',
  url(r'^(?P<object_id>\d+)/edit$',  'edit',  name='snippet_edit'),
  url(r'^(?P<object_id>\d+)/erase$', 'erase', name='snippet_erase'),
  )
