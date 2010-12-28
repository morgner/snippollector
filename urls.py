# -*- coding: utf8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
import os.path

admin.autodiscover()

urlpatterns = patterns('django.views.static',
  url(r'^robots\.txt$',            'serve', {'document_root':              settings.PROJECT_ROOT, 'path': 'templates/robots.txt', }),
  url(r'^favicon\.ico$',           'serve', {'document_root':              settings.PROJECT_ROOT, 'path': 'favicon.ico', }),
  url(r'^site-media/(?P<path>.*)', 'serve', {'document_root': os.path.join(settings.PROJECT_ROOT, 'site-media')}),
  url(r'^media/(?P<path>.*)',      'serve', {'document_root': os.path.join(settings.PROJECT_ROOT, 'media')}),
  )

urlpatterns += patterns('django.views.generic.simple',
  url(r'^$', 'redirect_to', {'url': '/snippets/'}),
  )

urlpatterns += patterns('',
  url(r'^snippets/', include('snippets.urls')),
  url(r'^admin/(.*)', admin.site.root),
  )

#urlpatterns += patterns('django.contrib.auth.views',
#  url(r'^accounts/login/$',                'login',                {'template_name': 'auth/login.html'},                name='login'),
#  url(r'^accounts/logout/$',               'logout',               {'template_name': 'auth/logged_out.html'},           name='logout'),
#  url(r'^accounts/password_change/$',      'password_change',      {'template_name': 'auth/password_change_form.html'}, name='pw_change'),
#  url(r'^accounts/password_change_done/$', 'password_change_done', {'template_name': 'auth/password_change_done.html'}, name='pw_change_done'),
#  )

#urlpatterns += patterns('snippets.views',
#  url(r'^siteindex.xml$',    'SiteIndex', name='site_index'),
#  )
