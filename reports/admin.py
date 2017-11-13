# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .views import simple_stats

# Register your models here.

admin.site.index_template = 'reports/index.html'

admin.site.register_view('reports/simple-stats', 'Jobs Stats', view=simple_stats, visible=True)

