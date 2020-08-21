# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse ,get_resolver

def home(request):
	context = {
	}
	return render(request, 'home.html', context)
