#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout
from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from erp import models

# Create your views here.
def Gaya_Home(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })

    return render_to_response('home.html', rctx)

def Gaya_Logout(request):
    logout(request)
    return HttpResponseRedirect('/')

def Emp_PWON(request):
    if request.POST.has_key('emp_id') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_id']) == 0:
            return HttpResponse('')
        else:
            gayaemp = models.GayaEmp.objects.get(id=int(request.POST['emp_id']))

    gayaemp.emp_pwon = 1

    try:
        gayaemp.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/index.html')

def ChangePW_Read(request, entry_id=None):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })

    return render_to_response('change_pw.html',rctx)

def ChangePW_Add(request):
    if request.POST.has_key('emp_pw') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_pw']) == 1:
            return HttpResponse('')
        else:
            pw = request.POST['emp_pw']

    if request.POST.has_key('emp_pwch') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_pwch']) == 1:
            return HttpResponse('')
        else:
            pwch = request.POST['emp_pwch']

    if pw == pwch:
        gayaemp = models.GayaEmp.objects.get(id=int(request.POST['emp_id']))
        gayaemp.password = pw
        #gayaemp.pwon = 1
        try:
            gayaemp.save()
        except:
            pass
    else:
        return HttpResponse('')

    return HttpResponseRedirect('home.html')
