#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

from erp import models
#from erp.forms import GayaForm02

import md5

# Create your views here.

#===Main
def Social_Main(request):
    gayascc = models.GayaSclCommon.objects.select_related().all().order_by('-id')[0:5]
    gayascf = models.GayaSclCommon.objects.select_related().all().order_by('-id')[0:5]
    gayascr = models.GayaSclCommon.objects.select_related().all().order_by('-id')[0:5]
    gayascq = models.GayaSclCommon.objects.select_related().all().order_by('-id')[0:5]

    rctx = RequestContext(request, {
        'gayascc' : gayascc,
        'gayascf' : gayascf,
        'gayascr' : gayascr,
        'gayascq' : gayascq,
    })

    return render_to_response('erp/social/main.html', rctx)

def Scc_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayascc = models.GayaSclCommon.objects.select_related().all().order_by('-scc_created')[start_pos:end_pos]
    total_page = (models.GayaSclCommon.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascc' : gayascc,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
        })
    elif (total_page/10*10+1) <= current_page and total_page >= current_page:
        for i in range(((total_page-1)/10*10+1), total_page):
            page_list.append(i)
        prev_page = current_page/10*10
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascc' : gayascc,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((page-1)/10*10+1, ((page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascc' : gayascc,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSclCommon.objects.count()

    return render_to_response('erp/social/scc.html', rctx)

def Scf_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayascf = models.GayaSclFree.objects.select_related().all().order_by('-scf_created')[start_pos:end_pos]
    total_page = (models.GayaSclFree.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascf' : gayascf,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
        })
    elif (total_page/10*10+1) <= current_page and total_page >= current_page:
        for i in range(((total_page-1)/10*10+1), total_page):
            page_list.append(i)
        prev_page = current_page/10*10
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascf' : gayascf,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((page-1)/10*10+1, ((page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascf' : gayascf,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayascf' : gayascf,
        'current_page' : page,
    })

    models.GayaSclFree.objects.count()

    return render_to_response('erp/social/scf.html', rctx)

def Scr_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayascr = models.GayaSclRecommend.objects.select_related().all().order_by('-scr_created')[start_pos:end_pos]
    total_page = (models.GayaSclRecommend.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascr' : gayascr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
        })
    elif (total_page/10*10+1) <= current_page and total_page >= current_page:
        for i in range(((total_page-1)/10*10+1), total_page):
            page_list.append(i)
        prev_page = current_page/10*10
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascr' : gayascr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((page-1)/10*10+1, ((page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascr' : gayascr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSclRecommend.objects.count()

    return render_to_response('erp/social/scr.html', rctx)

def Scq_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayascq = models.GayaSclQanda.objects.select_related().all().order_by('-scq_created')[start_pos:end_pos]
    total_page = (models.GayaSclQanda.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascq' : gayascq,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
        })
    elif (total_page/10*10+1) <= current_page and total_page >= current_page:
        for i in range(((total_page-1)/10*10+1), total_page):
            page_list.append(i)
        prev_page = current_page/10*10
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascq' : gayascq,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((page-1)/10*10+1, ((page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayascq' : gayascq,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSclQanda.objects.count()

    return render_to_response('erp/social/scq.html', rctx)

#===Read
def Scc_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclCommon.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_scc_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_scc_created()
    except:
        next_entry = ''

    comments = models.GayaSccComments.objects.filter(com_scc=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSclCommon.objects.count()

    return render_to_response('erp/social/read/scc.html', rctx)

def Scf_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclFree.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_scf_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_scf_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaSclFree.objects.count()

    return render_to_response('erp/social/read/scf.html', rctx)

def Scr_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclRecommend.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_scr_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_scr_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaSclRecommend.objects.count()

    return render_to_response('erp/social/read/scr.html', rctx)

def Scq_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclQanda.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_scq_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_scq_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaSclQanda.objects.count()

    return render_to_response('erp/social/read/scq.html', rctx)

#===Write
def Scc_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/social/write/scc.html', rctx)

def Scf_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/social/write/scf.html', rctx)

def Scr_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/social/write/scr.html', rctx)

def Scq_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/social/write/scq.html', rctx)

#===Add
@csrf_exempt
def Scc_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('scc_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scc_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['scc_title']

        if request.POST.has_key('scc_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scc_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['scc_name']

        if request.POST.has_key('scc_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scc_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['scc_pw']

        if request.POST.has_key('scc_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scc_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['scc_author']

        if request.POST.has_key('scc_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scc_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['scc_contents']

# 파일 처리
        if 'scc_file01' in request.FILES:
            file01 = request.FILES['scc_file01']
        else:
            file01 = 'none'
        if 'scc_file02' in request.FILES:
            file02 = request.FILES['scc_file02']
        else:
            file02 = 'none'
        if 'scc_file03' in request.FILES:
            file03 = request.FILES['scc_file03']
        else:
            file03 = 'none'
        if 'scc_img01' in request.FILES:
            img01 = request.FILES['scc_img01']
        else:
            img01 = 'none'
        if 'scc_img02' in request.FILES:
            img02 = request.FILES['scc_img02']
        else:
            img02 = 'none'
        if 'scc_img03' in request.FILES:
            img03 = request.FILES['scc_img03']
        else:
            img03 = 'none'

    else:
        pass

    new_entry = models.GayaSclCommon(scc_title=title, scc_name=name, scc_pw=pw, scc_contents=contents, scc_author=author,
            scc_file01=file01, scc_file02=file02, scc_file03=file03,
            scc_img01=img01, scc_img02=img02, scc_img03=img03 )

    #new_entry = models.GayaSclCommon(scc_title=title, scc_name=name, scc_pw=pw, scc_contents=contents,)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/scc.html')

@csrf_exempt
def Scf_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('scf_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scf_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['scf_title']

        if request.POST.has_key('scf_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scf_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['scf_name']

        if request.POST.has_key('scf_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scf_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['scf_pw']

        if request.POST.has_key('scf_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scf_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['scf_author']

        if request.POST.has_key('scf_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scf_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['scf_contents']

        if 'scf_file01' in request.FILES:
            file01 = request.FILES['scf_file01']
        else:
            file01 = 'none'
        if 'scf_file02' in request.FILES:
            file02 = request.FILES['scf_file02']
        else:
            file02 = 'none'
        if 'scf_file03' in request.FILES:
            file03 = request.FILES['scf_file03']
        else:
            file03 = 'none'
        if 'scf_img01' in request.FILES:
            img01 = request.FILES['scf_img01']
        else:
            img01 = 'none'
        if 'scf_img02' in request.FILES:
            img02 = request.FILES['scf_img02']
        else:
            img02 = 'none'
        if 'scf_img03' in request.FILES:
            img03 = request.FILES['scf_img03']
        else:
            img03 = 'none'

    else:
        pass

    new_entry = models.GayaSclFree(scf_title=title, scf_name=name, scf_pw=pw, scf_contents=contents, scf_author=author,
            scf_file01=file01, scf_file02=file02, scf_file03=file03,
            scf_img01=img01, scf_img02=img02, scf_img03=img03 )

    #new_entry = models.GayaSclFree(scf_title=title, scf_name=name, scf_pw=pw, scf_contents=contents,)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/scf.html')

@csrf_exempt
def Scr_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('scr_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scr_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['scr_title']

        if request.POST.has_key('scr_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scr_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['scr_name']

        if request.POST.has_key('scr_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scr_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['scr_pw']

        if request.POST.has_key('scr_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scr_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['scr_author']

        if request.POST.has_key('scr_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scr_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['scr_contents']

        if 'scr_file01' in request.FILES:
            file01 = request.FILES['scr_file01']
        else:
            file01 = 'none'
        if 'scr_file02' in request.FILES:
            file02 = request.FILES['scr_file02']
        else:
            file02 = 'none'
        if 'scr_file03' in request.FILES:
            file03 = request.FILES['scr_file03']
        else:
            file03 = 'none'
        if 'scr_img01' in request.FILES:
            img01 = request.FILES['scr_img01']
        else:
            img01 = 'none'
        if 'scr_img02' in request.FILES:
            img02 = request.FILES['scr_img02']
        else:
            img02 = 'none'
        if 'scr_img03' in request.FILES:
            img03 = request.FILES['scr_img03']
        else:
            img03 = 'none'

    else:
        pass

    new_entry = models.GayaSclRecommend(scr_title=title, scr_name=name, scr_pw=pw, scr_contents=contents, scr_author=author,
            scr_file01=file01, scr_file02=file02, scr_file03=file03,
            scr_img01=img01, scr_img02=img02, scr_img03=img03 )

    #new_entry = models.GayaSclRecommend(scr_title=title, scr_name=name, scr_pw=pw, scr_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/scr.html')

@csrf_exempt
def Scq_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('scq_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scq_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['scq_title']

        if request.POST.has_key('scq_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scq_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['scq_name']

        if request.POST.has_key('scq_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scq_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['scq_pw']

        if request.POST.has_key('scq_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scq_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['scq_author']

        if request.POST.has_key('scq_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['scq_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['scq_contents']

        if 'scq_file01' in request.FILES:
            file01 = request.FILES['scq_file01']
        else:
            file01 = 'none'
        if 'scq_file02' in request.FILES:
            file02 = request.FILES['scq_file02']
        else:
            file02 = 'none'
        if 'scq_file03' in request.FILES:
            file03 = request.FILES['scq_file03']
        else:
            file03 = 'none'
        if 'scq_img01' in request.FILES:
            img01 = request.FILES['scq_img01']
        else:
            img01 = 'none'
        if 'scq_img02' in request.FILES:
            img02 = request.FILES['scq_img02']
        else:
            img02 = 'none'
        if 'scq_img03' in request.FILES:
            img03 = request.FILES['scq_img03']
        else:
            img03 = 'none'

    else:
        pass

    new_entry = models.GayaSclQanda(scq_title=title, scq_name=name, scq_pw=pw, scq_contents=contents, scq_author=author,
            scq_file01=file01, scq_file02=file02, scq_file03=file03,
            scq_img01=img01, scq_img02=img02, scq_img03=img03 )

    #new_entry = models.GayaSclQanda(scq_title=title, scq_name=name, scq_pw=pw, scq_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/scq.html')

#===Modify
def Scc_Mod(request):
    page_title = ''

    current_entry = models.GayaSclCommon.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/social/modify/scc.html', rctx)

def Scf_Mod(request):
    page_title = ''

    current_entry = models.GayaSclFree.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/social/modify/scf.html', rctx)

def Scr_Mod(request):
    page_title = ''

    current_entry = models.GayaSclRecommend.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/social/modify/scr.html', rctx)

def Scq_Mod(request):
    page_title = ''

    current_entry = models.GayaSclQanda.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/social/modify/scq.html', rctx)

#===Del
def Scc_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclCommon.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/social/scc.html')

def Scf_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclFree.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/social/scf.html')

def Scr_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclRecommend.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/social/scr.html')

def Scq_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSclQanda.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/social/scq.html')

#===Comment_Add
@csrf_exempt
def Scc_Comadd(request):
# request에서 Comment 정보 추출
    name = request.POST.get('com_name', '')
    if not name.strip():
       return HttpResponse('')

    pw = request.POST.get('com_pw', '')
    if not pw.strip():
        return HttpResponse('')
    pw = md5.md5(pw).hexdigest()

    content = request.POST.get('com_content', '')
    if not content.strip():
        return HttpResponse('')

    entry = request.POST.get('entry_id', '')
    if not content.strip():
        return HttpResponse('')
    else:
        try:
            entry = models.GayaSclCommon.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaSccComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.scc_comments += 1 # Comment 카운팅
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/read/scc_read/%d' % int(entry.id))

@csrf_exempt
def Scf_Comadd(request):
    name = request.POST.get('com_name', '')
    if not name.strip():
       return HttpResponse('')

    pw = request.POST.get('com_pw', '')
    if not pw.strip():
        return HttpResponse('')
    pw = md5.md5(pw).hexdigest()

    content = request.POST.get('com_content', '')
    if not content.strip():
        return HttpResponse('')

    entry = request.POST.get('entry_id', '')
    if not content.strip():
        return HttpResponse('')
    else:
        try:
            entry = models.GayaSclFree.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaScfComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.scf_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/read/scf_read/%d' % int(entry.id))

@csrf_exempt
def Scr_Comadd(request):
    name = request.POST.get('com_name', '')
    if not name.strip():
       return HttpResponse('')

    pw = request.POST.get('com_pw', '')
    if not pw.strip():
        return HttpResponse('')
    pw = md5.md5(pw).hexdigest()

    content = request.POST.get('com_content', '')
    if not content.strip():
        return HttpResponse('')

    entry = request.POST.get('entry_id', '')
    if not content.strip():
        return HttpResponse('')
    else:
        try:
            entry = models.GayaSclRecommend.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaScrComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.scr_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/read/scr_read/%d' % int(entry.id))

@csrf_exempt
def Scq_Comadd(request):
    name = request.POST.get('com_name', '')
    if not name.strip():
       return HttpResponse('')

    pw = request.POST.get('com_pw', '')
    if not pw.strip():
        return HttpResponse('')
    pw = md5.md5(pw).hexdigest()

    content = request.POST.get('com_content', '')
    if not content.strip():
        return HttpResponse('')

    entry = request.POST.get('entry_id', '')
    if not content.strip():
        return HttpResponse('')
    else:
        try:
            entry = models.GayaSclQanda.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaScqComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.scq_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/social/read/scq_read/%d' % int(entry.id))

