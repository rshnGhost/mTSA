# importing required packages
import subprocess
import uuid
import os
import json

from dataStorage.models import phoneData
from dataStorage.models import phoneImg
from dataStorage.models import phoneBench
from dataStorage.models import PosTweet, NegTweet, NeuTweet, cache
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse#, HttpResponseRedirect, Http404
from django.views.decorators.csrf import csrf_exempt
#from base64 import b64encode

from django.conf import settings
from Twitter import process
from PostT import Tweet
#Twitter

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
#from fusioncharts import FusionCharts
#from account.forms import SignUpForm
#from account.tokens import account_activation_token

#from django.core import mail
from django.core.mail import send_mail

# disabling csrf (cross site request forgery)
@login_required
@csrf_exempt
def index(request):
	context = {}
	count = 0
	phone = phoneData.objects.all()
	count = len(phone)
	query = request.GET.get("q")
	if query:
		phone = phone.filter(
			Q(name__icontains=query)|
			Q(modelNo__icontains=query)
		).distinct()
		count = len(phone)
		if count == 0:
			cObject = cache.objects.create(
						name = query,
					    #tag = "search"
					    #satuts = models.BooleanField(default=False)
				)
			cObject.save()
			#except:
				#pass
	paginator = Paginator(phone, 6) # Show 25 contacts per page
	page_request_var = "page"
	page = request.GET.get(page_request_var)
	try:
		phone = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		phone = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		phone = paginator.page(paginator.num_pages)
	context = {
	"phone": phone,
	"count": count,
	"page_request_var": page_request_var,
	}
	return render(request, 'mobile/index.html', context)

@login_required
@csrf_exempt
def getdata(request, model):
	context = {}
	phone = phoneData.objects.get(modelNo = model)
	img = phoneImg.objects.filter(modelNo = model)
	bench = phoneBench.objects.get(modelNo = model)
	data = process("#"+phone.modelNo)

	dataPt = eval(data.ptweetst)
	#print("++++++")
	for dpt in (dataPt):
		#print(dpt['text'])
		#print(dpt['sentiment'])
		try:
			pObject = PosTweet.objects.create(
					##id = nId,
					posphone = phoneBench.objects.get(modelNo = model),
					tag = "#"+model,
					text = dpt['text']
			)
			pObject.save()
		except:
			pass
	dataNt = eval(data.ntweetst)
	#print("------")
	for dnt in (dataNt):
		#print(dnt['text'])
		#print(dnt['sentiment'])
		try:
			nObject = NegTweet.objects.create(
					##id = nId,
					negphone = phoneBench.objects.get(modelNo = model),
					tag = "#"+model,
					text = dnt['text']
			)
			nObject.save()
		except:
			pass
	dataNnt = eval(data.nntweetst)
	#print("======")
	for dnnt in (dataNnt):
		#print(dnnt['text'])
		#print(dnnt['sentiment'])
		try:
			nnObject = NeuTweet.objects.create(
					##id = nId,
					neuphone = phoneBench.objects.get(modelNo = model),
					tag = "#"+model,
					text = dnnt['text']
			)
			nnObject.save()
		except:
			pass
	bench.pt = bench.pt + data.pt
	bench.save()
	bench.nt = bench.nt + data.nt
	bench.save()
	bench.net = bench.net + data.net
	bench.save()
	bench.total = (bench.total + data.pt) - data.nt
	bench.save()
	context = {
		'img': img,
		'phone': phone,
		'data': data,
		'bench': bench
	}
	return render(request, 'mobile/mobile.html', context)


@login_required
@csrf_exempt
def showdata(request, model):
	context = {}
	bench = phoneBench.objects.get(modelNo = model)
	pTweet = PosTweet.objects.filter(posphone = bench)
	nTweet = NegTweet.objects.filter(negphone = bench)
	neTweet = NeuTweet.objects.filter(neuphone = bench)
	#data = process(model)
	context = {
		#'data': data,
		'bench': bench,
		'pTweet': pTweet,
		'nTweet': nTweet,
		'neTweet': neTweet
	}
	return render(request, 'mobile/mobileData.html', context)


@login_required
@csrf_exempt
def customPut(request):
	context = {}
	query = request.GET.get("tag")
	print(query)
	if query:
		data = process(query)
		#print(eval(data.ptweetst))
		dataPt = eval(data.ptweetst)
		dataNt = eval(data.ntweetst)
		dataNnt = eval(data.nntweetst)
		context = {
			'data': data,
			'dataPt': dataPt,
			'dataNt': dataNt,
			'dataNnt': dataNnt
		}
	return render(request, 'mobile/customTag.html', context)


@login_required
@csrf_exempt
def createTweet(request):
	context = {}
	query = request.POST.get("tweet")
	if query:
		#print( query )
		data = Tweet(query)
		#print(eval(str(data)))
		if str(data.status).isnumeric():
			mtext = "Tweet Added"
			messages.success(request, mtext)
		else:
			mtext = "Error Occured : "+ data.status
			messages.warning(request, mtext)
	return render(request, 'mobile/createTweet.html')
