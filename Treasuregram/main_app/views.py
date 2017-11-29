# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# a python function that takes in a web requests that returns a web response
#Views are used to run functions in response to specific URLs
def index(request):
	return HttpResponse('<h1>Hello Explorers!</h1>')
	#need to map this view to a URL 