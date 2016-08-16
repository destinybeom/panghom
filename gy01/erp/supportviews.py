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

# Create your views here.

#===Main
def Support_Main(request):
    gayastl = models.GayaSptLinux.objects.select_related().all().order_by('-id')[0:5]
    gayastw = models.GayaSptWindows.objects.select_related().all().order_by('-id')[0:5]
    gayastv = models.GayaSptServer.objects.select_related().all().order_by('-id')[0:5]
    gayastt = models.GayaSptStorage.objects.select_related().all().order_by('-id')[0:5]
    gayastc = models.GayaSptSwitch.objects.select_related().all().order_by('-id')[0:5]
    gayastd = models.GayaSptDev.objects.select_related().all().order_by('-id')[0:5]

    rctx = RequestContext(request, {
        'gayastl' : gayastl,
        'gayastw' : gayastw,
        'gayastv' : gayastv,
        'gayastt' : gayastt,
        'gayastc' : gayastc,
        'gayastd' : gayastd,
    })

    return render_to_response('erp/support/main.html', rctx)

def Stl_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayastl = models.GayaSptLinux.objects.select_related().all().order_by('-stl_created')[start_pos:end_pos]
    total_page = (models.GayaSptLinux.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayastl' : gayastl,
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
            'gayastl' : gayastl,
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
            'gayastl' : gayastl,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSptLinux.objects.count()

    return render_to_response('erp/support/stl.html', rctx)

def Stw_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayastw = models.GayaSptWindows.objects.select_related().all().order_by('-stw_created')[start_pos:end_pos]
    total_page = (models.GayaSptWindows.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayastw' : gayastw,
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
            'gayastw' : gayastw,
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
            'gayastw' : gayastw,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSptWindows.objects.count()

    return render_to_response('erp/support/stw.html', rctx)

def Stv_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayastv = models.GayaSptServer.objects.select_related().all().order_by('-stv_created')[start_pos:end_pos]
    total_page = (models.GayaSptServer.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayastv' : gayastv,
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
            'gayastv' : gayastv,
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
            'gayastv' : gayastv,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSptServer.objects.count()

    return render_to_response('erp/support/stv.html', rctx)

def Stt_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayastt = models.GayaSptStorage.objects.select_related().all().order_by('-stt_created')[start_pos:end_pos]
    total_page = (models.GayaSptStorage.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayastt' : gayastt,
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
            'gayastt' : gayastt,
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
            'gayastt' : gayastt,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSptStorage.objects.count()

    return render_to_response('erp/support/stt.html', rctx)

def Stc_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayastc = models.GayaSptSwitch.objects.select_related().all().order_by('-stc_created')[start_pos:end_pos]
    total_page = (models.GayaSptSwitch.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayastc' : gayastc,
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
            'gayastc' : gayastc,
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
            'gayastc' : gayastc,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSptSwitch.objects.count()

    return render_to_response('erp/support/stc.html', rctx)

def Std_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayastd = models.GayaSptDev.objects.select_related().all().order_by('-std_created')[start_pos:end_pos]
    total_page = (models.GayaSptDev.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayastd' : gayastd,
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
            'gayastd' : gayastd,
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
            'gayastd' : gayastd,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaSptDev.objects.count()

    return render_to_response('erp/support/std.html', rctx)

#===Read
def Stl_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptLinux.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_stl_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_stl_created()
    except:
        next_entry = ''

    comments = models.GayaStlComments.objects.filter(com_stl=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSptLinux.objects.count()

    return render_to_response('erp/support/read/stl.html', rctx)

def Stw_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptWindows.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_stw_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_stw_created()
    except:
        next_entry = ''

    comments = models.GayaStwComments.objects.filter(com_stw=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSptWindows.objects.count()

    return render_to_response('erp/support/read/stw.html', rctx)

def Stv_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptServer.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_stv_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_stv_created()
    except:
        next_entry = ''

    comments = models.GayaStvComments.objects.filter(com_stv=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSptServer.objects.count()

    return render_to_response('erp/support/read/stv.html', rctx)

def Stt_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptStorage.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_stt_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_stt_created()
    except:
        next_entry = ''

    comments = models.GayaSttComments.objects.filter(com_stt=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSptStorage.objects.count()

    return render_to_response('erp/support/read/stt.html', rctx)

def Stc_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptSwitch.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_stc_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_stc_created()
    except:
        next_entry = ''

    comments = models.GayaStcComments.objects.filter(com_stc=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSptSwitch.objects.count()

    return render_to_response('erp/support/read/stc.html', rctx)

def Std_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptDev.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_std_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_std_created()
    except:
        next_entry = ''

    comments = models.GayaStdComments.objects.filter(com_std=current_entry).order_by('com_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'comments' : comments,
    })

    models.GayaSptDev.objects.count()

    return render_to_response('erp/support/read/std.html', rctx)

#===Write
def Stl_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/support/write/stl.html', rctx)

def Stw_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/support/write/stw.html', rctx)

def Stv_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/support/write/stv.html', rctx)

def Stt_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/support/write/stt.html', rctx)

def Stc_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/support/write/stc.html', rctx)

def Std_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/support/write/std.html', rctx)

#===Add
@csrf_exempt
def Stl_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('stl_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stl_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['stl_title']

        if request.POST.has_key('stl_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stl_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['stl_name']

        if request.POST.has_key('stl_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stl_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['stl_pw']

        if request.POST.has_key('stl_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stl_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['stl_author']

        if request.POST.has_key('stl_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stl_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['stl_contents']

        if 'stl_file01' in request.FILES:
            file01 = request.FILES['stl_file01']
        else:
            file01 = 'none'
        if 'stl_file02' in request.FILES:
            file02 = request.FILES['stl_file02']
        else:
            file02 = 'none'
        if 'stl_file03' in request.FILES:
            file03 = request.FILES['stl_file03']
        else:
            file03 = 'none'
        if 'stl_file04' in request.FILES:
            file04 = request.FILES['stl_file04']
        else:
            file04 = 'none'
        if 'stl_file05' in request.FILES:
            file05 = request.FILES['stl_file05']
        else:
            file05 = 'none'
        if 'stl_img01' in request.FILES:
            img01 = request.FILES['stl_img01']
        else:
            img01 = 'none'
        if 'stl_img02' in request.FILES:
            img02 = request.FILES['stl_img02']
        else:
            img02 = 'none'
        if 'stl_img03' in request.FILES:
            img03 = request.FILES['stl_img03']
        else:
            img03 = 'none'
        if 'stl_img04' in request.FILES:
            img04 = request.FILES['stl_img04']
        else:
            img04 = 'none'
        if 'stl_img05' in request.FILES:
            img05 = request.FILES['stl_img05']
        else:
            img05 = 'none'

    else:
        pass

    new_entry = models.GayaSptLinux(stl_title=title, stl_name=name, stl_pw=pw, stl_contents=contents, stl_author=author,
            stl_file01=file01, stl_file02=file02, stl_file03=file03, stl_file04=file04, stl_file05=file05,
            stl_img01=img01, stl_img02=img02, stl_img03=img03, stl_img04=img04, stl_img05=img05)

    #new_entry = models.GayaSptLinux(stl_title=title, stl_name=name, stl_pw=pw, stl_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/stl.html')

@csrf_exempt
def Stw_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('stw_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stw_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['stw_title']

        if request.POST.has_key('stw_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stw_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['stw_name']

        if request.POST.has_key('stw_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stw_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['stw_pw']

        if request.POST.has_key('stw_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stw_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['stw_author']

        if request.POST.has_key('stw_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stw_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['stw_contents']

        if 'stw_file01' in request.FILES:
            file01 = request.FILES['stw_file01']
        else:
            file01 = 'none'
        if 'stw_file02' in request.FILES:
            file02 = request.FILES['stw_file02']
        else:
            file02 = 'none'
        if 'stw_file03' in request.FILES:
            file03 = request.FILES['stw_file03']
        else:
            file03 = 'none'
        if 'stw_file04' in request.FILES:
            file04 = request.FILES['stw_file04']
        else:
            file04 = 'none'
        if 'stw_file05' in request.FILES:
            file05 = request.FILES['stw_file05']
        else:
            file05 = 'none'
        if 'stw_img01' in request.FILES:
            img01 = request.FILES['stw_img01']
        else:
            img01 = 'none'
        if 'stw_img02' in request.FILES:
            img02 = request.FILES['stw_img02']
        else:
            img02 = 'none'
        if 'stw_img03' in request.FILES:
            img03 = request.FILES['stw_img03']
        else:
            img03 = 'none'
        if 'stw_img04' in request.FILES:
            img04 = request.FILES['stw_img04']
        else:
            img04 = 'none'
        if 'stw_img05' in request.FILES:
            img05 = request.FILES['stw_img05']
        else:
            img05 = 'none'

    else:
        pass

    new_entry = models.GayaSptWindows(stw_title=title, stw_name=name, stw_pw=pw, stw_contents=contents, stw_author=author,
            stw_file01=file01, stw_file02=file02, stw_file03=file03, stw_file04=file04, stw_file05=file05,
            stw_img01=img01, stw_img02=img02, stw_img03=img03, stw_img04=img04, stw_img05=img05)

    #new_entry = models.GayaSptWindows(stw_title=title, stw_name=name, stw_pw=pw, stw_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/stw.html')

@csrf_exempt
def Stv_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('stv_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stv_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['stv_title']

        if request.POST.has_key('stv_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stv_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['stv_name']

        if request.POST.has_key('stv_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stv_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['stv_pw']

        if request.POST.has_key('stv_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stv_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['stv_author']

        if request.POST.has_key('stv_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stv_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['stv_contents']

        if 'stv_file01' in request.FILES:
            file01 = request.FILES['stv_file01']
        else:
            file01 = 'none'
        if 'stv_file02' in request.FILES:
            file02 = request.FILES['stv_file02']
        else:
            file02 = 'none'
        if 'stv_file03' in request.FILES:
            file03 = request.FILES['stv_file03']
        else:
            file03 = 'none'
        if 'stv_file04' in request.FILES:
            file04 = request.FILES['stv_file04']
        else:
            file04 = 'none'
        if 'stv_file05' in request.FILES:
            file05 = request.FILES['stv_file05']
        else:
            file05 = 'none'
        if 'stv_img01' in request.FILES:
            img01 = request.FILES['stv_img01']
        else:
            img01 = 'none'
        if 'stv_img02' in request.FILES:
            img02 = request.FILES['stv_img02']
        else:
            img02 = 'none'
        if 'stv_img03' in request.FILES:
            img03 = request.FILES['stv_img03']
        else:
            img03 = 'none'
        if 'stv_img04' in request.FILES:
            img04 = request.FILES['stv_img04']
        else:
            img04 = 'none'
        if 'stv_img05' in request.FILES:
            img05 = request.FILES['stv_img05']
        else:
            img05 = 'none'

    else:
        pass

    new_entry = models.GayaSptServer(stv_title=title, stv_name=name, stv_pw=pw, stv_contents=contents, stv_author=author,
            stv_file01=file01, stv_file02=file02, stv_file03=file03, stv_file04=file04, stv_file05=file05,
            stv_img01=img01, stv_img02=img02, stv_img03=img03, stv_img04=img04, stv_img05=img05)

    #new_entry = models.GayaSptServer(stv_title=title, stv_name=name, stv_pw=pw, stv_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/stv.html')

@csrf_exempt
def Stt_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('stt_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stt_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['stt_title']

        if request.POST.has_key('stt_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stt_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['stt_name']

        if request.POST.has_key('stt_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stt_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['stt_pw']

        if request.POST.has_key('stt_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stt_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['stt_author']

        if request.POST.has_key('stt_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stt_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['stt_contents']

        if 'stt_file01' in request.FILES:
            file01 = request.FILES['stt_file01']
        else:
            file01 = 'none'
        if 'stt_file02' in request.FILES:
            file02 = request.FILES['stt_file02']
        else:
            file02 = 'none'
        if 'stt_file03' in request.FILES:
            file03 = request.FILES['stt_file03']
        else:
            file03 = 'none'
        if 'stt_file04' in request.FILES:
            file04 = request.FILES['stt_file04']
        else:
            file04 = 'none'
        if 'stt_file05' in request.FILES:
            file05 = request.FILES['stt_file05']
        else:
            file05 = 'none'
        if 'stt_img01' in request.FILES:
            img01 = request.FILES['stt_img01']
        else:
            img01 = 'none'
        if 'stt_img02' in request.FILES:
            img02 = request.FILES['stt_img02']
        else:
            img02 = 'none'
        if 'stt_img03' in request.FILES:
            img03 = request.FILES['stt_img03']
        else:
            img03 = 'none'
        if 'stt_img04' in request.FILES:
            img04 = request.FILES['stt_img04']
        else:
            img04 = 'none'
        if 'stt_img05' in request.FILES:
            img05 = request.FILES['stt_img05']
        else:
            img05 = 'none'

    else:
        pass

    new_entry = models.GayaSptStorage(stt_title=title, stt_name=name, stt_pw=pw, stt_contents=contents, stt_author=author,
            stt_file01=file01, stt_file02=file02, stt_file03=file03, stt_file04=file04, stt_file05=file05,
            stt_img01=img01, stt_img02=img02, stt_img03=img03, stt_img04=img04, stt_img05=img05)

    #new_entry = models.GayaSptStorage(stt_title=title, stt_name=name, stt_pw=pw, stt_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/stt.html')

@csrf_exempt
def Stc_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('stc_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stc_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['stc_title']

        if request.POST.has_key('stc_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stc_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['stc_name']

        if request.POST.has_key('stc_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stc_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['stc_pw']

        if request.POST.has_key('stc_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stc_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['stc_author']

        if request.POST.has_key('stc_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['stc_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['stc_contents']

        if 'stc_file01' in request.FILES:
            file01 = request.FILES['stc_file01']
        else:
            file01 = 'none'
        if 'stc_file02' in request.FILES:
            file02 = request.FILES['stc_file02']
        else:
            file02 = 'none'
        if 'stc_file03' in request.FILES:
            file03 = request.FILES['stc_file03']
        else:
            file03 = 'none'
        if 'stc_file04' in request.FILES:
            file04 = request.FILES['stc_file04']
        else:
            file04 = 'none'
        if 'stc_file05' in request.FILES:
            file05 = request.FILES['stc_file05']
        else:
            file05 = 'none'
        if 'stc_img01' in request.FILES:
            img01 = request.FILES['stc_img01']
        else:
            img01 = 'none'
        if 'stc_img02' in request.FILES:
            img02 = request.FILES['stc_img02']
        else:
            img02 = 'none'
        if 'stc_img03' in request.FILES:
            img03 = request.FILES['stc_img03']
        else:
            img03 = 'none'
        if 'stc_img04' in request.FILES:
            img04 = request.FILES['stc_img04']
        else:
            img04 = 'none'
        if 'stc_img05' in request.FILES:
            img05 = request.FILES['stc_img05']
        else:
            img05 = 'none'

    else:
        pass

    new_entry = models.GayaSptSwitch(stc_title=title, stc_name=name, stc_pw=pw, stc_contents=contents, stc_author=author,
            stc_file01=file01, stc_file02=file02, stc_file03=file03, stc_file04=file04, stc_file05=file05,
            stc_img01=img01, stc_img02=img02, stc_img03=img03, stc_img04=img04, stc_img05=img05)

    #new_entry = models.GayaSptSwitch(stc_title=title, stc_name=name, stc_pw=pw, stc_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/stc.html')

@csrf_exempt
def Std_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('std_title') == False:
            return HttpResponse('')
        else:
            if len(request.POST['std_title']) == 0:
                return HttpResponse('')
            else:
                title = request.POST['std_title']

        if request.POST.has_key('std_name') == False:
            return HttpResponse('')
        else:
            if len(request.POST['std_name']) == 0:
                return HttpResponse('')
            else:
                name = request.POST['std_name']

        if request.POST.has_key('std_pw') == False:
            return HttpResponse('')
        else:
            if len(request.POST['std_pw']) == 0:
                return HttpResponse('')
            else:
                pw = request.POST['std_pw']

        if request.POST.has_key('std_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['std_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['std_author']

        if request.POST.has_key('std_contents') == False:
            return HttpResponse('')
        else:
            if len(request.POST['std_contents']) == 0:
                return HttpResponse('')
            else:
                contents = request.POST['std_contents']

        if 'std_file01' in request.FILES:
            file01 = request.FILES['std_file01']
        else:
            file01 = 'none'
        if 'std_file02' in request.FILES:
            file02 = request.FILES['std_file02']
        else:
            file02 = 'none'
        if 'std_file03' in request.FILES:
            file03 = request.FILES['std_file03']
        else:
            file03 = 'none'
        if 'std_file04' in request.FILES:
            file04 = request.FILES['std_file04']
        else:
            file04 = 'none'
        if 'std_file05' in request.FILES:
            file05 = request.FILES['std_file05']
        else:
            file05 = 'none'
        if 'std_img01' in request.FILES:
            img01 = request.FILES['std_img01']
        else:
            img01 = 'none'
        if 'std_img02' in request.FILES:
            img02 = request.FILES['std_img02']
        else:
            img02 = 'none'
        if 'std_img03' in request.FILES:
            img03 = request.FILES['std_img03']
        else:
            img03 = 'none'
        if 'std_img04' in request.FILES:
            img04 = request.FILES['std_img04']
        else:
            img04 = 'none'
        if 'std_img05' in request.FILES:
            img05 = request.FILES['std_img05']
        else:
            img05 = 'none'

    else:
        pass

    new_entry = models.GayaSptDev(std_title=title, std_name=name, std_pw=pw, std_contents=contents, std_author=author,
            std_file01=file01, std_file02=file02, std_file03=file03, std_file04=file04, std_file05=file05,
            std_img01=img01, std_img02=img02, std_img03=img03, std_img04=img04, std_img05=img05)

    #new_entry = models.GayaSptDev(std_title=title, std_name=name, std_pw=pw, std_contents=contents)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/std.html')

#===Mod
def Stl_Mod(request):
    page_title = ''

    current_entry = models.GayaSptLinux.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/support/modify/stl.html', rctx)

def Stw_Mod(request):
    page_title = ''

    current_entry = models.GayaSptWindows.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/support/modify/stw.html', rctx)

def Stv_Mod(request):
    page_title = ''

    current_entry = models.GayaSptServer.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/support/modify/stv.html', rctx)

def Stt_Mod(request):
    page_title = ''

    current_entry = models.GayaSptStorage.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/support/modify/stt.html', rctx)

def Stc_Mod(request):
    page_title = ''

    current_entry = models.GayaSptSwitch.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/support/modify/stc.html', rctx)

def Std_Mod(request):
    page_title = ''

    current_entry = models.GayaSptDev.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/support/modify/std.html', rctx)

#===Del
def Stl_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptLinux.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/support/stl.html')

def Stw_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptWindows.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/support/stw.html')

def Stv_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptServer.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/support/stv.html')

def Stt_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptStorage.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/support/stt.html')

def Stc_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptSwitch.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/support/stc.html')

def Std_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaSptDev.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/support/std.html')

#===Comment_Add
@csrf_exempt
def Stl_Comadd(request):
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
            entry = models.GayaSptLinux.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaStlComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.stl_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/read/stl_read/%d' % int(entry.id))

@csrf_exempt
def Stw_Comadd(request):
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
            entry = models.GayaSptWindows.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaStwComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.stw_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/read/stw_read/%d' % int(entry.id))

@csrf_exempt
def Stv_Comadd(request):
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
            entry = models.GayaSptServer.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaStvComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.stv_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/read/stw_read/%d' % int(entry.id))

@csrf_exempt
def Stt_Comadd(request):
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
            entry = models.GayaSptStorage.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaSttComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.stt_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/read/stt_read/%d' % int(entry.id))

@csrf_exempt
def Stc_Comadd(request):
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
            entry = models.GayaSptSwitch.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaStcComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.stc_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/read/stc_read/%d' % int(entry.id))

@csrf_exempt
def Std_Comadd(request):
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
            entry = models.GayaSptDev.objects.get(id=request.POST['entry_id'])
        except:
            return HttpResponse('')

    try:
        new_comment = models.GayaStdComments(com_name=name, com_pw=pw, com_contents=content, com_scc=entry)
        new_comment.save()
        entry.std_comments += 1
        entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/support/read/std_read/%d' % int(entry.id))

