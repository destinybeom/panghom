#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from erp import models

# Create your views here.

def Gaya_Main(request):
    page_title = ''

    gayascc = models.GayaSclCommon.objects.select_related().all().order_by('-id')[0:5]
    gayaord = models.GayaOrder.objects.select_related().all().order_by('-id')[0:5]

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayascc' : gayascc,
        'gayaord' : gayaord,
    })

    return render_to_response('erp/index.html', rctx)

def Gaya_About(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })

    return render_to_response('erp/about.html', rctx)
