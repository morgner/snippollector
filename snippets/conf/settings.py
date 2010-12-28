# -*- coding: utf-8 -*-

from django.conf import settings

# application specific settings

PAGINATE_BY = getattr( settings, "SNIPPETS_PAGINATE_BY", 10)
