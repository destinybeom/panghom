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

import re

# Create your views here.

#===Main
def Mgmt_Main(request):
    page_title = ''

    gayacus = models.GayaCustomer.objects.select_related().all().order_by('-id')[0:5]
    gayapro = models.GayaProductInfo.objects.select_related().all().order_by('-id')[0:5]
    gayamtr = models.GayaMaterialInfo.objects.select_related().all().order_by('-id')[0:5]
    gayaord = models.GayaOrder.objects.select_related().all().order_by('-id')[0:5]
    #gayapsn = models.GayaProductSN.objects.select_related().all().order_by('-id')[0:5]
    gayamsn = models.GayaMaterialSN.objects.select_related().all().order_by('-id')[0:5]

    cusCnt = len(gayacus)
    proCnt = len(gayapro)
    mtrCnt = len(gayamtr)
    ordCnt = len(gayaord)
    #psnCnt = len(gayapsn)
    mtrCnt = len(gayamsn)

    rctx = RequestContext(request, {
        'gayacus' : gayacus,
        'gayapro' : gayapro,
        'gayamtr' : gayamtr,
        'gayaord' : gayaord,
        #'gayapsn' : gayapsn,
        'gayamsn' : gayamtr,
        'cusCnt' : cusCnt,
        'proCnt' : proCnt,
        'mtrCnt' : mtrCnt,
        'ordCnt' : ordCnt,
        #'psnCnt' : psnCnt,
        'msnCnt' : mtrCnt,
    })
    return render_to_response('erp/mgmt/main.html', rctx)

def Emp_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

#모든 테이블의 기본 키값인 id 컬럼으로 start_pos~end_pos까지 조회
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')[start_pos:end_pos]
#GayaEMP 테이블에 등록되어 있는 로우를 카운트하고 현재 페이지를 차감한 페이지의 수를 확인
    total_page = (models.GayaEmp.objects.select_related().all().count()-1)/20+1

#페이지처리(10페이지단위로 블럭처리)
#10페이지가 넘어가지 않으면 첫 블럭으로 인식
    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
        })
#10단위 페이지의 제일 마지막 블럭 계산
    elif (total_page/10*10+1) <= current_page and total_page >= current_page:
        for i in range(((total_page-1)/10*10+1), total_page):
            page_list.append(i)
        prev_page = current_page/10*10
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
#첫 블럭과 마지막 블럭이 아닐경우 처리
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaEmp.objects.count()

    return render_to_response('erp/mgmt/emp.html', rctx)

def Cus_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayacus = models.GayaCustomer.objects.select_related().all().order_by('-cus_created')[start_pos:end_pos]
    total_page = (models.GayaCustomer.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayacus' : gayacus,
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
            'gayacus' : gayacus,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayacus' : gayacus,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaCustomer.objects.count()

    return render_to_response('erp/mgmt/cus.html', rctx)

def Pro_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayapro = models.GayaProductInfo.objects.select_related().all()
    total_page = (models.GayaProductInfo.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayapro' : gayapro,
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
            'gayapro' : gayapro,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayapro' : gayapro,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaProductInfo.objects.count()

    return render_to_response('erp/mgmt/pro.html', rctx)

def HA201TP_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    ha201tp = models.HA201_TP.objects.select_related().all().order_by('-pro_created')[start_pos:end_pos]
    total_page = (models.HA201_TP.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'ha201tp' : ha201tp,
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
            'ha201tp' : ha201tp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'ha201tp' : ha201tp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.HA201_TP.objects.count()

    return render_to_response('erp/mgmt/HA201_TP.html', rctx)

def Mtr_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayamtr = models.GayaMaterialInfo.objects.select_related().all().order_by('-mtr_created')[start_pos:end_pos]
    total_page = (models.GayaMaterialInfo.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamtr' : gayamtr,
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
            'gayamtr' : gayamtr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamtr' : gayamtr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaMaterialInfo.objects.count()

    return render_to_response('erp/mgmt/mtr.html', rctx)

def Ord_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayaord = models.GayaOrder.objects.select_related().all().order_by('-ord_created')[start_pos:end_pos]
    total_page = (models.GayaOrder.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaord' : gayaord,
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
            'gayaord' : gayaord,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaord' : gayaord,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaOrder.objects.count()

    return render_to_response('erp/mgmt/ord.html', rctx)

def Msn_Main(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayamsn = models.GayaMaterialSN.objects.select_related().all().order_by('-msn_created')[start_pos:end_pos]
    total_page = (models.GayaMaterialSN.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamsn' : gayamsn,
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
            'gayamsn' : gayamsn,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamsn' : gayamsn,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaMaterialSN.objects.count()

    return render_to_response('erp/mgmt/msn.html', rctx)

#===Read
def Emp_Read(request, entry_id=None):
    page_title = ''

#웹에서 넘어온 entry_id 값으로 조회
    current_entry = models.GayaEmp.objects.get(id=int(entry_id))

#현재 조회된 값의 앞뒤 값 조회
    try:
        prev_entry = current_entry.get_previous_by_emp_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_emp_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaEmp.objects.count()

    return render_to_response('erp/mgmt/read/emp.html', rctx)

def Cus_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaCustomer.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_cus_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_cus_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaCustomer.objects.count()

    return render_to_response('erp/mgmt/read/cus.html', rctx)

def Pro_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaProductInfo.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_pro_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_pro_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaProductInfo.objects.count()

    return render_to_response('erp/mgmt/read/pro.html', rctx)

def HA201TP_Read(request, entry_id=None):
    page_title = ''

#HA201_TP의 정보 조회
    ha201tp = models.HA201_TP.objects.get(id=int(entry_id))

    current_entry = []
    entry_cnt = []

#HA201_TP의 조회된 값으로 부품을 다시 조회하여 리스트에 추가
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Disk_Backplane'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Interposer'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='SSD'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Power_Housing'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Power_Supply'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Chassis'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='CPU'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='DRAM'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Mainboard'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='RMM4_light'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='SATADOM'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Expander_Board'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Riser_Card_Left'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='FC_HBA'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Riser_Card_Right'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='Host_Bus_Adapter'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='NTB'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='NVRAM'))
    current_entry.append(models.GayaMaterialSN.objects.filter(msn_psn=ha201tp.pro_sn, msn_class='FAN'))

#부품들의 수를 카운팅
    for entry in current_entry:
        entry_cnt.append(entry.count())

#HA201_TP의 앞뒤 값 조회
    try:
        prev_entry = ha201tp.get_previous_by_ha201tp_created()
    except:
        prev_entry = ''

    try:
        next_entry = ha201tp.get_next_by_ha201tp_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'ha201tp' : ha201tp,
        'current_entry' : current_entry,
        'entry_cnt' : entry_cnt,
    })

    models.HA201_TP.objects.count()

    return render_to_response('erp/mgmt/read/ha201_tp.html', rctx)

def Mtr_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaMaterialInfo.objects.get(id=int(entry_id))

    try:
        usingCnt = models.GayaMaterialSN.objects.filter(msn_mtr=current_entry, msn_using=1).count()
    except:
        usingCnt = 0

    try:
        outCnt = models.GayaMaterialSN.objects.filter(msn_mtr=current_entry, msn_out=1).count()
    except:
        outCnt = 0

    try:
        prev_entry = current_entry.get_previous_by_mtr_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_mtr_created()
    except:
        next_entry = ''

    remnants = int(current_entry.mtr_total) - int(outCnt)
    usingCnt = int(usingCnt) - int(outCnt)

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
        'remnants' : remnants,
        'usingCnt' : usingCnt,
        'outCnt' : outCnt,
    })

    models.GayaMaterialInfo.objects.count()

    return render_to_response('erp/mgmt/read/mtr.html', rctx)

def Ord_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaOrder.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_ord_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_ord_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaOrder.objects.count()

    return render_to_response('erp/mgmt/read/ord.html', rctx)

def Msn_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaMaterialSN.objects.get(id=int(entry_id))

    try:
        prev_entry = current_entry.get_previous_by_msn_created()
    except:
        prev_entry = ''

    try:
        next_entry = current_entry.get_next_by_msn_created()
    except:
        next_entry = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaMaterialSN.objects.count()

    return render_to_response('erp/mgmt/read/msn.html', rctx)

#===Write
def Emp_Write(request):
    page_title = ''

    rctx = RequestContext(request, {
        'page_title' : page_title,
    })
    return render_to_response('erp/mgmt/write/emp.html', rctx)

def Cus_Write(request):
    page_title = ''

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/mgmt/write/cus.html', rctx)

def Pro_Write(request):
    page_title = ''

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/mgmt/write/pro.html', rctx)

def HA201TP_Write(request):
    page_title = ''

    ha201tp_emp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'ha201tp_emp' : ha201tp_emp,
    })
    return render_to_response('erp/mgmt/write/ha201_tp.html', rctx)

def Mtr_Write(request):
    page_title = ''

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/mgmt/write/mtr.html', rctx)

def Ord_Write(request):
    page_title = ''

    gayapro = models.GayaProductInfo.objects.select_related().all()
    gayacus = models.GayaCustomer.objects.select_related().all().order_by('-cus_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayapro' : gayapro,
        'gayacus' : gayacus,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/mgmt/write/ord.html', rctx)

def Msn_Write(request):
    page_title = ''

    gayamtr = models.GayaMaterialInfo.objects.filter(mtr_finished_sn=0).order_by('-mtr_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayamtr' : gayamtr,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/mgmt/write/msn.html', rctx)

#===Add
@csrf_exempt
def Emp_Add(request):
#request를 넘겨받아 내부 항목의 값을 조회
    if request.POST.has_key('emp_name') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_name']) == 1:
            return HttpResponse('')
        else:
            name = request.POST['emp_name']

    if request.POST.has_key('emp_rank') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_rank']) == 0:
            return HttpResponse('')
        else:
            rank = request.POST['emp_rank']

    if request.POST.has_key('emp_phone') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_phone']) == 0:
            return HttpResponse('')
        else:
            phone = request.POST['emp_phone']

    if request.POST.has_key('emp_email') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_email']) == 0:
            return HttpResponse('')
        else:
            email = request.POST['emp_email']

    if request.POST.has_key('emp_address') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_address']) == 0:
            return HttpResponse('')
        else:
            address = request.POST['emp_address']

    if request.POST.has_key('emp_job') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_job']) == 0:
            return HttpResponse('')
        else:
            job = request.POST['emp_job']

    if request.POST.has_key('emp_birthday') == False:
        return HttpResponse('')
    else:
        if len(request.POST['emp_birthday']) == 0:
            return HttpResponse('')
        else:
            birthday = request.POST['emp_birthday']

    if request.POST.has_key('emp_note') == False:
        note = ''
    else:
        if len(request.POST['emp_note']) == 0:
            note = ''
        else:
            note = request.POST['emp_note']

#조회된 값을 등록
    new_entry = models.GayaEmp(emp_name=name, emp_rank=rank, emp_phone=phone, emp_email=email, emp_address=address,
            emp_job=job, emp_birthday=birthday, emp_note=note)

#등록된 값을 DB에 저장
    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/mgmt/emp.html')

@csrf_exempt
def Cus_Add(request):
    if request.POST.has_key('cus_name') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_name']) == 0:
            return HttpResponse('')
        else:
            name = request.POST['cus_name']

    if request.POST.has_key('cus_section') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_section']) == 0:
            return HttpResponse('')
        else:
            section = request.POST['cus_section']

    if request.POST.has_key('cus_rsps') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_rsps']) == 0:
            return HttpResponse('')
        else:
            rsps = request.POST['cus_rsps']

    if request.POST.has_key('cus_rank') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_rank']) == 0:
            return HttpResponse('')
        else:
            rank = request.POST['cus_rank']

    if request.POST.has_key('cus_department') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_department']) == 0:
            return HttpResponse('')
        else:
            department = request.POST['cus_department']

    if request.POST.has_key('cus_phone') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_phone']) == 0:
            return HttpResponse('')
        else:
            phone = request.POST['cus_phone']

    if request.POST.has_key('cus_rphone') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_rphone']) == 0:
            return HttpResponse('')
        else:
            rphone = request.POST['cus_rphone']

    if request.POST.has_key('cus_email') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_email']) == 0:
            return HttpResponse('')
        else:
            email = request.POST['cus_email']

    if request.POST.has_key('cus_address') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_address']) == 0:
            return HttpResponse('')
        else:
            address = request.POST['cus_address']

    if request.POST.has_key('cus_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['cus_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('cus_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['cus_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['cus_author']

    if request.POST.has_key('cus_note') == False:
        note = ''
    else:
        if len(request.POST['cus_note']) == 0:
            note = ''
        else:
            note = request.POST['cus_note']

    new_entry = models.GayaCustomer(cus_name=name, cus_section=section, cus_rsps=rsps, cus_rank=rank, cus_department=department,
            cus_phone=phone, cus_rphone=rphone, cus_email=email, cus_address=address, cus_emp=emp, cus_author=author, cus_note=note)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/mgmt/cus.html')

@csrf_exempt
def Pro_Add(request):
    if request.POST.has_key('pro_class') == False:
        return HttpResponse('1')
    else:
        if len(request.POST['pro_class']) == 0:
            return HttpResponse('1')
        else:
            pClass = request.POST['pro_class']

    if request.POST.has_key('pro_name') == False:
        return HttpResponse('2')
    else:
        if len(request.POST['pro_name']) == 0:
            return HttpResponse('2')
        else:
            name = request.POST['pro_name']

    if request.POST.has_key('pro_info') == False:
        return HttpResponse('3')
    else:
        if len(request.POST['pro_info']) == 0:
            return HttpResponse('3')
        else:
            info = request.POST['pro_info']

    if request.POST.has_key('pro_emp') == False:
        return HttpResponse('4')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['pro_emp'])
        except:
            return HttpResponse('4')

    if request.POST.has_key('pro_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['pro_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['pro_author']

    if request.POST.has_key('pro_note') == False:
        note = ''
    else:
        if len(request.POST['pro_note']) == 0:
            note = ''
        else:
            note = request.POST['pro_note']

    new_entry = models.GayaProductInfo(pro_class=pClass, pro_name=name, pro_info=info, pro_emp=emp, pro_author=author, pro_note=note)

    try:
        new_entry.save()
    except:
        return HttpResponse('5')
    return HttpResponseRedirect('/erp/mgmt/pro.html')

@csrf_exempt
def HA201TP_Add(request):
#PN과 SN을 검사하기위한 정규식
    chk = re.compile(r"([\w-]+)")

#HA201_TP의 PN과 SN을 구분하기 위한 리스트
    HA201TP_PIN = [
        'disk_backplane_pn'        , 'interposer_pn'            , 'ssd_pn'
        , 'power_housing_pn'         , 'power_supply_pn'          , 'p_chassis_pn'           , 'p_cpu_pn'
        , 'p_dram_pn'                , 'p_mainboard_pn'           , 'p_rmm4_light_pn'        , 'p_satadom_pn'
        , 'p_expander_board_pn'      , 'p_riser_card_l_pn'        , 'p_fc_hba_pn'            , 'p_riser_card_r_pn'
        , 'p_host_bus_adapter_pn'    , 'p_ntb_pn'                 , 'p_nvram_pn'             , 'p_fan_pn'
        , 's_chassis_pn'             , 's_cpu_pn'                 , 's_dram_pn'              , 's_mainboard_pn'
        , 's_rmm4_light_pn'          , 's_satadom_pn'             , 's_expander_board_pn'    , 's_riser_card_l_pn'
        , 's_fc_hba_pn'              , 's_riser_card_r_pn'        , 's_host_bus_adapter_pn'  , 's_ntb_pn'
        , 's_nvram_pn'               , 's_fan_pn'
    ]
    HA201TP_SIN = [
        'disk_backplane_sn'        , 'interposer_sn'            , 'ssd_sn'
        , 'power_housing_sn'         , 'power_supply_sn'          , 'p_chassis_sn'           , 'p_cpu_sn'
        , 'p_dram_sn'                , 'p_mainboard_sn'           , 'p_rmm4_light_sn'        , 'p_satadom_sn'
        , 'p_expander_board_sn'      , 'p_riser_card_l_sn'        , 'p_fc_hba_sn'            , 'p_riser_card_r_sn'
        , 'p_host_bus_adapter_sn'    , 'p_ntb_sn'                 , 'p_nvram_sn'             , 'p_fan_sn'
        , 's_chassis_sn'             , 's_cpu_sn'                 , 's_dram_sn'              , 's_mainboard_sn'
        , 's_rmm4_light_sn'          , 's_satadom_sn'             , 's_expander_board_sn'    , 's_riser_card_l_sn'
        , 's_fc_hba_sn'              , 's_riser_card_r_sn'        , 's_host_bus_adapter_sn'  , 's_ntb_sn'
        , 's_nvram_sn'               , 's_fan_sn'
    ]

#추출한 PN와 SN를 저장하기 위한 사전
    HA201TP_POUT = {}
    HA201TP_SOUT = {}

#추출한 정보를 중복제거 후 저장하는 리스트
    HA201TP_PN = []
    HA201TP_SN = []

#DB에 등록되어 있는 부품과 매칭이 안되는 key 리스트
    WRONG_KEYS = []

#실제 DB에 등록될 최종 데이터
    HA201TP_VALUES = [
        ''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''    ,''   ,''
        ,''    ,''    ,''    ,''
    ]
    # 값이 잘못되었을 경우 표시할 페이지 식별자
    REDIRECT_KEY = 0

#request에서 HA201_TP의 기본 정보 추출
    if request.POST.has_key('pro_pn') == False:
        return HttpResponse('')
    else:
        if len(request.POST['pro_pn']) == 0:
            pn = '(x)'
        else:
            pn = request.POST['pro_pn']

    if request.POST.has_key('pro_sn') == False:
        return HttpResponse('')
    else:
        if len(request.POST['pro_sn']) == 0:
            sn = '(x)'
        else:
            sn = request.POST['pro_sn']

    if request.POST.has_key('pro_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['pro_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('pro_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['pro_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['pro_author']

    if request.POST.has_key('pro_note') == False:
        note = ''
    else:
        if len(request.POST['pro_note']) == 0:
            note = ''
        else:
            note = request.POST['pro_note']

#request에서 PN 추출
    for v in HA201TP_PIN:
        if request.POST.has_key(v) == False:
            HA201TP_POUT[v] = '(x)'
        else:
            if len(request.POST[v]) == 0:
                HA201TP_POUT[v] = '(x)'
            else:
                HA201TP_POUT[v] = request.POST[v]
                HA201TP_PN.extend(chk.findall(request.POST[v]))

#request에서 SN 추출
    for v in HA201TP_SIN:
        if request.POST.has_key(v) == False:
            HA201TP_SOUT[v] = '(x)'
        else:
            if len(request.POST[v]) == 0:
                HA201TP_SOUT[v] = '(x)'
            else:
                HA201TP_SOUT[v] = request.POST[v]
                HA201TP_SN.extend(chk.findall(request.POST[v]))

#HA201_TP 제품 등록이 안될 경우 제일 먼저 확인할 로그
    #print len(HA201TP_PN), len(HA201TP_SN), len(HA201TP_VALUES)

#request에서 추출한 PN과 SN을 카운팅하여 타입확인
#PN는 중복될 수 있기 때문에 분리
#pnList는 중복될 가능성이 있는 PN를 제거한 리스트
#조건에 맞으면 pnList의 번호로 입력된 PN를 조회
    if len(HA201TP_PN) == 35 and len(HA201TP_SN) == len(HA201TP_VALUES):
        pnList = [0,24,48,49,51,52,54,62,63,64,66,67,68,69,71,72,73,74,75,77,78,80,88,89,90,92,93,94,95,97,98,99,100,101]
        pnCnt = 0
        for i in range(104): #입력된 정보의 수 = 리스트의 길이
            #입력된 PN와 등록된 PN를 확인
            try: #입력된 SN으로 HA201_TP 조회, 조회가 성공하면 SN는 일치
                HA201TP_VALUES[i] = models.GayaMaterialSN.objects.get(msn_sn=HA201TP_SN[i])
                if HA201TP_PN[pnCnt] == HA201TP_VALUES[i].msn_pn:
                    pass
                else: # 맞지 않을 경우
                    if '(x)' in HA201TP_PN[pnCnt]: #(x) 이미 등록되어 있다면 pass
                        pass
                    else: # (x)가 없다면 추가
                        HA201TP_PN[pnCnt] += '_(x)'
                        # 잘못된 값으로 인한 pnCnt 수정
                        if pnCnt > 12 and pnCnt <= 27:
                            WRONG_KEYS.append(HA201TP_PIN[pnCnt-1])
                        elif pnCnt > 27:
                            WRONG_KEYS.append(HA201TP_PIN[pnCnt-2])
                        else:
                            WRONG_KEYS.append(HA201TP_PIN[pnCnt])
                    REDIRECT_KEY = 1
            except: # 입력된 SN으로 조회가 안되었을 경우, 입력된 SN은 잘못된 값
                try: # 입력된 PN으로 다시 조회, 조회되면 PN은 일치
                    temp = models.GayaMaterialSN.objects.get(msn_pn=HA201TP_PN[pnCnt])
                    HA201TP_SN[i] += '_(x)'
                    if pnCnt > 12 and pnCnt <= 27:
                        WRONG_KEYS.append(HA201TP_SIN[pnCnt-1])
                    elif pnCnt > 27:
                        WRONG_KEYS.append(HA201TP_SIN[pnCnt-2])
                    else:
                        WRONG_KEYS.append(HA201TP_SIN[pnCnt])
                    REDIRECT_KEY = 1
                except: # 입력된 PN으로 조회가 안되어 PN까지 잘못된 값
                    if '(x)' in HA201TP_PN[pnCnt]:
                        pass
                    else:
                        HA201TP_PN[pnCnt] += '_(x)'
                        # 잘못된 값으로 인한 pnCnt 수정
                        if pnCnt > 12 and pnCnt <= 27:
                            WRONG_KEYS.append(HA201TP_PIN[pnCnt-1])
                            WRONG_KEYS.append(HA201TP_SIN[pnCnt-1])
                        elif pnCnt > 27:
                            WRONG_KEYS.append(HA201TP_PIN[pnCnt-2])
                            WRONG_KEYS.append(HA201TP_SIN[pnCnt-2])
                        else:
                            WRONG_KEYS.append(HA201TP_PIN[pnCnt])
                            WRONG_KEYS.append(HA201TP_SIN[pnCnt])
                    HA201TP_SN[i] += '_(x)'
                    REDIRECT_KEY = 1
            if i in pnList:
                pnCnt += 1

    elif len(HA201TP_PN) == 33 and len(HA201TP_SN) == len(HA201TP_VALUES):
        pnList = [0,24,48,49,51,52,54,62,63,64,66,67,69,71,72,73,74,75,77,78,80,88,89,90,92,93,95,97,98,99,100,101]
        pnCnt = 0
        for i in range(104):
            try:
                HA201TP_VALUES[i] = models.GayaMaterialSN.objects.get(msn_sn=HA201TP_SN[i])
                if HA201TP_PN[pnCnt] == HA201TP_VALUES[i].msn_pn:
                    pass
                else:
                    if '(x)' in HA201TP_PN[pnCnt]:
                        pass
                    else:
                        HA201TP_PN[pnCnt] += '_(x)'
                        WRONG_KEYS.append(HA201TP_PIN[pnCnt])
                    REDIRECT_KEY = 2
            except:
                try:
                    temp = models.GayaMaterialSN.objects.get(msn_pn=HA201TP_PN[pnCnt])
                    HA201TP_SN[i] += '_(x)'
                    WRONG_KEYS.append(HA201TP_SIN[pnCnt])
                    REDIRECT_KEY = 2
                except:
                    if '(x)' in HA201TP_PN[pnCnt]:
                        pass
                    else:
                        HA201TP_PN[pnCnt] += '_(x)'
                        WRONG_KEYS.append(HA201TP_PIN[pnCnt])
                        WRONG_KEYS.append(HA201TP_SIN[pnCnt])
                    HA201TP_SN[i] += '_(x)'
                    REDIRECT_KEY = 2
            if i in pnList:
                pnCnt += 1

# 최초 모든 값을 입력할 경우
    elif len(HA201TP_PN) == len(HA201TP_SN) == len(HA201TP_VALUES):
        #for i in len(HA201TP_VALUES):
        for i in range(104):
            try:
                HA201TP_VALUES[i] = models.GayaMaterialSN.objects.get(msn_sn=HA201TP_SN[i])
                if HA201TP_PN[i] == HA201TP_VALUES[i].msn_pn:
                    pass
                else:
                    HA201TP_PN[i] += '_(x)'
                    REDIRECT_KEY = 3
            except:
                try:
                    temp = models.GayaMaterialSN.objects.get(msn_pn=HA201TP_PN[i])
                    HA201TP_SN[i] += '_(x)'
                    REDIRECT_KEY = 3
                except:
                    HA201TP_PN[i] += '_(x)'
                    HA201TP_SN[i] += '_(x)'
                    REDIRECT_KEY = 3

    else:
        page_title = ''

        gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'pro_pout' : HA201TP_POUT,
            'pro_sout' : HA201TP_SOUT,
            'pro_pn' : pn,
            'pro_sn' : sn,
            'pro_emp' : emp,
            'pro_note' : note,
        })
        return render_to_response('erp/mgmt/write/ha201_tp_01.html', rctx)

# 입력된 값이 잘못되었을 경우의 페이지
    if REDIRECT_KEY == 1:
        page_title = ''

        gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'pro_pout' : HA201TP_PN,
            'pro_sout' : HA201TP_SN,
            'wrong_keys' : WRONG_KEYS,
            'pro_pn' : pn,
            'pro_sn' : sn,
            'pro_emp' : emp,
            'pro_note' : note,
        })
        return render_to_response('erp/mgmt/write/ha201_tp_02.html', rctx)

    elif REDIRECT_KEY == 2:
        page_title = ''

        gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'pro_pout' : HA201TP_PN,
            'pro_sout' : HA201TP_SN,
            'wrong_keys' : WRONG_KEYS,
            'pro_pn' : pn,
            'pro_sn' : sn,
            'pro_emp' : emp,
            'pro_note' : note,
        })
        return render_to_response('erp/mgmt/write/ha201_tp_03.html', rctx)

    elif REDIRECT_KEY == 3:
        page_title = ''

        gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'pro_pout' : HA201TP_PN,
            'pro_sout' : HA201TP_SN,
            'pro_pn' : pn,
            'pro_sn' : sn,
            'pro_emp' : emp,
            'pro_note' : note,
        })
        return render_to_response('erp/mgmt/write/ha201_tp_04.html', rctx)

    else:
        pass

#값들이 모두 확인되면 등록
    new_entry = models.HA201_TP(pro_name='HA201_TP', pro_class='Storage', pro_pn=pn, pro_sn=sn, pro_emp=emp,
            pro_state=0, pro_using=0, pro_out=0, pro_author=author, pro_note=note)

    try:
        new_entry.save()
        try: # 부품에 HA201_TP에 할당되었다는 정보 등록
            eNum = 0
            eStr = ''
            for i, msn in enumerate(HA201TP_VALUES):
                msn.msn_pro = 'HA201_TP'
                msn.msn_psn = sn # <---
                msn.msn_using = 1 # <---
                try:
                    msn.save()
                except: # 부품등록이 안될 경우
                    eNum = 1
                    eStr = eStr + ', ' + str(i)
                    if eNum != 0:
                        return HttpResponse('%s'%eStr)
        except:
            return HttpResponse('??')
    except:
        return HttpResponse('%s에서 문제가 발생하였습니다. 확인 후 다시 진행하십시오.'%(sn))
    return HttpResponseRedirect('/erp/mgmt/HA201_TP.html')

@csrf_exempt
def Mtr_Add(request):
    if request.POST.has_key('mtr_class') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_class']) == 0:
            return HttpResponse('')
        else:
            mClass = request.POST['mtr_class']

    if request.POST.has_key('mtr_name') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_name']) == 0:
            return HttpResponse('')
        else:
            name = request.POST['mtr_name']

    if request.POST.has_key('mtr_desc') == False:
        desc = ''
    else:
        if len(request.POST['mtr_desc']) == 0:
            desc = ''
        else:
            desc = request.POST['mtr_desc']

    if request.POST.has_key('mtr_total') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_total']) == 0:
            return HttpResponse('')
        else:
            total = request.POST['mtr_total']

    if request.POST.has_key('mtr_maker') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_maker']) == 0:
            return HttpResponse('')
        else:
            maker = request.POST['mtr_maker']

    if request.POST.has_key('mtr_purchase') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_purchase']) == 0:
            return HttpResponse('')
        else:
            purchase = request.POST['mtr_purchase']

    if request.POST.has_key('mtr_purchaseday') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_purchaseday']) == 0:
            return HttpResponse('')
        else:
            purchaseday = request.POST['mtr_purchaseday']

    if request.POST.has_key('mtr_repository') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_repository']) == 0:
            return HttpResponse('')
        else:
            repository = request.POST['mtr_repository']
            if '기타' == repository:
                repository = request.POST['mtr_rpst']

    if request.POST.has_key('mtr_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['mtr_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('mtr_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['mtr_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['mtr_author']

    if request.POST.has_key('mtr_note') == False:
        note = ''
    else:
        if len(request.POST['mtr_note']) == 0:
            note = ''
        else:
            note = request.POST['mtr_note']

    new_entry = models.GayaMaterialInfo(mtr_class=mClass, mtr_name=name, mtr_desc=desc, mtr_total=total, mtr_maker=maker, mtr_purchase=purchase,
            mtr_purchaseday=purchaseday, mtr_repository=repository, mtr_emp=emp, mtr_author=author, mtr_note=note)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/mgmt/mtr.html')

@csrf_exempt
def Ord_Add(request):
    if request.POST.has_key('ord_title') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_title']) == 0:
            return HttpResponse('')
        else:
            title = request.POST['ord_title']

    if request.POST.has_key('ord_ponum') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_ponum']) == 0:
            return HttpResponse('')
        else:
            ponum = request.POST['ord_ponum']

    if request.POST.has_key('ord_pro') == False:
        return HttpResponse('')
    else:
        try:
            pro = models.GayaProductInfo.objects.get(id=request.POST['ord_pro'])
        except:
            return HttpResponse('')

    if request.POST.has_key('ord_cus') == False:
        return HttpResponse('')
    else:
        try:
            cus = models.GayaCustomer.objects.get(id=request.POST['ord_cus'])
        except:
            return HttpResponse('')

    if request.POST.has_key('ord_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['ord_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('ord_total') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_total']) == 0:
            return HttpResponse('')
        else:
            total = request.POST['ord_total']

    if request.POST.has_key('ord_os') == False:
        os = 'none'
    else:
        if len(request.POST['ord_os']) == 0:
            os = 'none'
        else:
            os = request.POST['ord_os']

    if request.POST.has_key('ord_orderday') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_orderday']) == 0:
            return HttpResponse('')
        else:
            orderday = request.POST['ord_orderday']

    if request.POST.has_key('ord_delivery') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_delivery']) == 0:
            return HttpResponse('')
        else:
            delivery = request.POST['ord_delivery']

    if request.POST.has_key('ord_warranty') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_warranty']) == 0:
            return HttpResponse('')
        else:
            warranty = request.POST['ord_warranty']

    if request.POST.has_key('ord_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['ord_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['ord_author']

    if request.POST.has_key('ord_note') == False:
        note = ''
    else:
        if len(request.POST['ord_note']) == 0:
            note = ''
        else:
            note = request.POST['ord_note']

    new_entry = models.GayaOrder(ord_title=title, ord_ponum=ponum, ord_pro=pro, ord_cus=cus, ord_emp=emp, ord_total=total,
            ord_os=os, ord_orderday=orderday, ord_delivery=delivery, ord_warranty=warranty, ord_author=author, ord_note=note)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/mgmt/ord.html')

@csrf_exempt
def Msn_Add(request):
# 다수의 SN을 구분하기 위한 정규식
    chk = re.compile(r"([\w-]+)")
    pson = 0
    if request.POST.has_key('msn_mtr') == False:
        return HttpResponse('')
    else:
        try:
            mtr = models.GayaMaterialInfo.objects.get(id=request.POST['msn_mtr'])
        except:
            return HttpResponse('')

    if request.POST.has_key('msn_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['msn_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('msn_pn') == False:
        return HttpResponse('')
    else: # PN 중복 처리
        if len(request.POST['msn_pn']) == 0:
            if int(request.POST['pn_equal']) == 0:
                pn = models.GayaMaterialSN.objects.filter(msn_mtr=mtr).order_by('id')[0].msn_pn
                if 'gaya' in pn:
                    pson = 2
        else:
            pn = request.POST['msn_pn']
            if 'gaya' in pn:
                try:
                    temp_pn_cnt = int(models.GayaMaterialSN.objects.filter(msn_pson=2|3).order_by('-id')[0].msn_pn.split('-')[1])
                    pn = 'gaya-' + str(temp_pn_cnt+1)
                except:
                    temp_pn_cnt = 0
                    pn = 'gaya-' + str(temp_pn_cnt+1)
                pson = 2

    if request.POST.has_key('msn_sn') == False:
        return HttpResponse('')
    else:
        if len(request.POST['msn_sn']) == 0:
            return HttpResponse('')
        else:
            snList = chk.findall(request.POST['msn_sn']) # 다수의 SN을 구분하여 리스트에 저장

    if request.POST.has_key('msn_state') == False:
        return HttpResponse('')
    else:
        if len(request.POST['msn_state']) == 0:
            return HttpResponse('')
        else:
            state = request.POST['msn_state']

    if request.POST.has_key('msn_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['msn_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['msn_author']

    if request.POST.has_key('msn_note') == False:
        note = ''
    else:
        if len(request.POST['msn_note']) == 0:
            note = ''
        else:
            note = request.POST['msn_note']

    try:
        temp_sn_cnt = int(models.GayaMaterialSN.objects.filter(msn_pson=1|3).order_by('-id')[0].msn_sn.split('-')[1])
    except:
        temp_sn_cnt = 0
    for sn in snList: # 다수의 SN을 저장
        if 'gaya' in sn: # 임시 SN일 경우
            sn = 'gaya-' + str(temp_sn_cnt+1)
            if pson == 0:
                pson = 1
                new_entry = models.GayaMaterialSN(msn_mtr=mtr, msn_class=mtr.mtr_class, msn_emp=emp, msn_pn=pn, msn_sn=sn,
                        msn_state=state, msn_author=author, msn_note=note, msn_pson=pson)
            else:
                pson = 3
                new_entry = models.GayaMaterialSN(msn_mtr=mtr, msn_class=mtr.mtr_class, msn_emp=emp, msn_pn=pn, msn_sn=sn,
                        msn_state=state, msn_author=author, msn_note=note, msn_pson=pson)
        else:
            new_entry = models.GayaMaterialSN(msn_mtr=mtr, msn_class=mtr.mtr_class, msn_emp=emp, msn_pn=pn, msn_sn=sn,
                    msn_state=state, msn_author=author, msn_note=note, msn_pson=pson)

        try:
            new_entry.save()
        except:
            return HttpResponse('%s에서 문제가 발생했습니다. 확인 후 다시 진행하십시오.'%(sn))

    try:
        msnCnt = models.GayaMaterialSN.objects.filter(msn_mtr=mtr).count()
    except:
        pass

# 부품구입정보의 수와 등록된 부품의 수가 같으면 등록 완료 처리
    if mtr.mtr_total >= msnCnt:
        mtr.mtr_finished_sn = 1
        try:
            mtr.save()
        except:
            pass
    else:
        pass

    return HttpResponseRedirect('/erp/mgmt/msn.html')

#===Mod
def Emp_Mod(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaEmp.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })

    return render_to_response('erp/mgmt/modify/emp.html', rctx)

def Cus_Mod(request):
    page_title = ''

    current_entry = models.GayaCustomer.objects.get(id=int(entry_id))

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaemp' : gayaemp,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/mgmt/modify/cus.html', rctx)

def Pro_Mod(request):
    page_title = ''

    current_entry = models.GayaProductInfo.objects.get(id=int(entry_id))

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/mgmt/modify/pro.html', rctx)

def HA201TP_Mod(request):
    page_title = ''

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')
    gayamsn = models.GayaMaterialSN.objects.select_related().all().order_by('-msn_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaemp' : gayaemp,
        'gayamsn' : gayamsn,
    })
    return render_to_response('erp/mgmt/modify/ha201tp.html', rctx)

def Mtr_Mod(request):
    page_title = ''

    current_entry = models.GayaMaterialInfo.objects.get(id=int(entry_id))

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaemp' : gayaemp,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/mgmt/modify/mtr.html', rctx)

def Ord_Mod(request):
    page_title = ''

    current_entry = models.GayaOrder.objects.get(id=int(entry_id))

    gayapro = models.GayaProductInfo.objects.select_related().all().order_by('-pro_created')
    gayacus = models.GayaCustomer.objects.select_related().all().order_by('-cus_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayapro' : gayapro,
        'gayacus' : gayacus,
        'gayaemp' : gayaemp,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/mgmt/modify/ord.html', rctx)

def Msn_Mod(request):
    page_title = ''

    current_entry = models.GayaMaterialSN.objects.get(id=int(entry_id))

    gayamtr = models.GayaMaterialInfo.objects.select_related().all().order_by('-mtr_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayamtr' : gayamtr,
        'gayaemp' : gayaemp,
        'current_entry' : current_entry,
    })
    return render_to_response('erp/mgmt/modify/msn.html', rctx)

#===Del
def Emp_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaEmp.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/emp.html')

def Cus_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaCustomer.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/cus.html')

def Pro_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaProductInfo.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/pro.html')

def HA201TP_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.HA201_TP.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/ha201tp.html')

def Mtr_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaMaterialInfo.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/mtr.html')

def Ord_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaOrder.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/ord.html')

def Msn_Del(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaMaterialSN.objects.get(id=int(entry_id))

    try:
        current_entry.delete()
    except:
        return HttpResponse('')

    return HttpResponseRedirect('/erp/mgmt/msn.html')

#===Search
def Emp_Search(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')[start_pos:end_pos]
    total_page = (models.GayaEmp.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
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
            'gayaemp' : gayaemp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaemp' : gayaemp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaEmp.objects.count()

    return render_to_response('erp/mgmt/emp.html', rctx)

def Cus_Search(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayacus = models.GayaCustomer.objects.select_related().all().order_by('-cus_created')[start_pos:end_pos]
    total_page = (models.GayaCustomer.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayacus' : gayacus,
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
            'gayacus' : gayacus,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayacus' : gayacus,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaCustomer.objects.count()

    return render_to_response('erp/mgmt/cus.html', rctx)

def Pro_Search(request, page=1):
    current_page = int(current_page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayapro = models.GayaProductInfo.objects.select_related().all()
    total_page = (models.GayaProductInfo.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayapro' : gayapro,
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
            'gayapro' : gayapro,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayapro' : gayapro,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaProductInfo.objects.count()

    return render_to_response('erp/mgmt/pro.html', rctx)

def HA201TP_Search(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    ha201tp = models.HA201_TP.objects.select_related().all().order_by('-ha201tp_created')[start_pos:end_pos]
    total_page = (models.HA201_TP.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'ha201tp' : ha201tp,
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
            'ha201tp' : ha201tp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'ha201tp' : ha201tp,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.HA201_TP.objects.count()

    return render_to_response('erp/mgmt/HA201_TP.html', rctx)

def Mtr_Search(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayamtr = models.GayaMaterialInfo.objects.select_related().all().order_by('-mtr_created')[start_pos:end_pos]
    total_page = (models.GayaMaterialInfo.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamtr' : gayamtr,
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
            'gayamtr' : gayamtr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamtr' : gayamtr,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaMaterialInfo.objects.count()

    return render_to_response('erp/mgmt/mtr.html', rctx)

def Ord_Search(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayaord = models.GayaOrder.objects.select_related().all().order_by('-ord_created')[start_pos:end_pos]
    total_page = (models.GayaOrder.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaord' : gayaord,
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
            'gayaord' : gayaord,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayaord' : gayaord,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaOrder.objects.count()

    return render_to_response('erp/mgmt/ord.html', rctx)

def Msn_Search(request, page=1):
    current_page = int(page)
    per_page = 20
    start_pos = (current_page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''
    page_list = []

    gayamsn = models.GayaMaterialSN.objects.select_related().all().order_by('-msn_created')[start_pos:end_pos]
    total_page = (models.GayaMaterialSN.objects.select_related().all().count()-1)/20+1

    if total_page <= 11:
        for i in range(1, total_page):
            page_list.append(i)
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamsn' : gayamsn,
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
            'gayamsn' : gayamsn,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
        })
    else:
        for i in range((current_page-1)/10*10+1, ((current_page-1)/10+1)*10+1):
            page_list.append(i)
        prev_page = current_page/10*10
        next_page = current_page/10*10+1
        rctx = RequestContext(request, {
            'page_title' : page_title,
            'gayamsn' : gayamsn,
            'current_page' : current_page,
            'total_page' : total_page,
            'page_list' : page_list,
            'prev_page' : prev_page,
            'next_page' : next_page,
        })

    models.GayaMaterialSN.objects.count()

    return render_to_response('erp/mgmt/msn.html', rctx)

