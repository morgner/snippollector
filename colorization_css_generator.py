#!/usr/bin/env python
import os.path
from pygments.formatters import HtmlFormatter

path = 'site-media/css/syntax.css'
f = open(path,'w')
f.write(HtmlFormatter(style='fruity').get_style_defs('.highlight'))
f.close()