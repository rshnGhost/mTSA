# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import phoneData
from .models import phoneImg
from .models import phoneBench
from .models import PosTweet, NegTweet, NeuTweet
from .models import cache, phoneWeb, antutu

class PosTweetInline(admin.TabularInline):#StackedInline
	model = PosTweet
	extra = 0

class NegTweetInline(admin.TabularInline):#StackedInline
	model = NegTweet
	extra = 0

class NeuTweetInline(admin.TabularInline):#StackedInline
	model = NeuTweet
	extra = 0

class phoneDataAdmin(admin.ModelAdmin):
	list_display = ["name", "modelNo", "price", "picture"]
	list_display_links = ["name"]
	list_editable = ["price"]
	list_filter = ["name", "modelNo"]
	search_fields = ["modelNo", "name"]

	class Meta:
		model = phoneData

class phoneBenchAdmin(admin.ModelAdmin):
	list_display = ["device", "pt", "nt", "net", "cpu", "gpu", "mem", "ux", "total" ]
	list_display_links = ["device"]
	#list_editable = ["pt", "net", "nt"]
	list_filter = ["device", "total"]
	search_fields = ["modelNo"]
	inlines = [PosTweetInline, NegTweetInline, NeuTweetInline]

	class Meta:
		model = phoneBench

class cacheAdmin(admin.ModelAdmin):
	list_display = ["name", "tag", "satuts" ]
	list_display_links = ["name"]
	list_editable = ["satuts"]
	list_filter = ["name", "satuts"]

	class Meta:
		model = cache
# Register your models here.

admin.site.register(phoneData, phoneDataAdmin)
admin.site.register(phoneImg)
admin.site.register(antutu)
admin.site.register(PosTweet)
admin.site.register(NegTweet)
admin.site.register(NeuTweet)
admin.site.register(phoneWeb)
admin.site.register(cache, cacheAdmin)
admin.site.register(phoneBench, phoneBenchAdmin)
