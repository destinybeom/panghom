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
def State_Main(request):
    page_title = ''

    gayascc = models.GayaSclCommon.objects.select_related().all().order_by('-id')[0:5]
    gayaord = models.GayaOrder.objects.select_related().all().order_by('-id')[0:5]

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayascc' : gayascc,
        'gayaord' : gayaord,
    })

    return render_to_response('erp/state/main.html', rctx)

def Ord_Main(request, page=1):
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''

    assign_ord = {}
    aOrd = models.GayaOrder.objects.filter(ord_complete=1) # 주문할당

    complete_ord = models.GayaOrder.objects.filter(ord_complete=2) # 주문완료
    ready_ord = models.GayaOrder.objects.filter(ord_complete=0) # 주문

    cOrd_cnt = complete_ord.count()
    aOrd_cnt = aOrd.count()
    rOrd_cnt = ready_ord.count()

    gayadlr = []
# 주문 관련 Report 정보 조회
    for order in aOrd:
        gayaorr = models.OrderReport.objects.filter(orr_ord=order)
        gOrr_cnt = gayaorr.count()
        for orr in gayaorr:
            gDlr_cnt = models.DeliveryReport.objects.filter(dlr_orr=orr).count()
        assign_ord[order] = [gOrr_cnt, gDlr_cnt]

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'complete_ord' : complete_ord,
        'assign_ord'   : assign_ord,
        'ready_ord'    : ready_ord,
        'cOrd_cnt'     : cOrd_cnt,
        'aOrd_cnt'     : aOrd_cnt,
        'rOrd_cnt'     : rOrd_cnt,
    })

    return render_to_response('erp/state/ord.html', rctx)

def Pro_Main(request, page=1):
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''

    gayapro = models.GayaProductInfo.objects.select_related().all()

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayapro' : gayapro,
    })

    return render_to_response('erp/state/pro.html', rctx)

def Mtr_Main(request, page=1):
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''

    mList = []

# 부품별 정보 조회
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Disk_Backplane'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Interposer'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='SSD'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Power_Housing'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Power_Supply'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Chassis'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='CPU'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='DRAM'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Mainboard'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='RMM4_light'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='SATADOM'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Expander_Board'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Riser_Card_Left'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='FC_HBA'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Riser_Card_Right'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='Host_Bus_Adapter'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='NTB'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='NVRAM'))
    mList.append(models.GayaMaterialSN.objects.filter(msn_class='FAN'))

    infoDic = {}
    for i, m in enumerate(mList):
        try:
            tCnt = 0
            yCnt = 0
            for st in m:
                tCnt += 1
                if st.msn_state == 0:
                    yCnt += 1
        except:
            yCnt = 0
            tCnt = 0

        try:
            nCnt = tCnt - yCnt
        except:
            nCnt = 0

        #try:
        #    uCnt = 0
        #    for st in m:
        #        if st.msn_using <= 1:
        #            uCnt += 1
        #except:
        #    uCnt = 0

        try:
            oCnt = 0
            for st in m:
                if st.msn_out == 1:
                    oCnt += 1
        except:
            oCnt = 0

        # 구매수량, 등록수량, 미등록수량, 사용수량, 출고수량, 자재정보
        infoDic[i] = [tCnt, yCnt, nCnt, oCnt, m]

    Disk_Backplane    =  infoDic[0]
    Interposer        =  infoDic[1]
    SSD               =  infoDic[2]
    Power_Housing     =  infoDic[3]
    Power_Supply      =  infoDic[4]
    Chassis           =  infoDic[5]
    CPU               =  infoDic[6]
    DRAM              =  infoDic[7]
    Mainboard         =  infoDic[8]
    RMM4_light        =  infoDic[9]
    SATADOM           =  infoDic[10]
    Expander_Board    =  infoDic[11]
    Riser_Card_Left   =  infoDic[12]
    FC_HBA            =  infoDic[13]
    Riser_Card_Right  =  infoDic[14]
    Host_Bus_Adapter  =  infoDic[15]
    NTB               =  infoDic[16]
    NVRAM             =  infoDic[17]
    FAN               =  infoDic[18]

    rctx = RequestContext(request, {
        'page_title'        : page_title,
        'Disk_Backplane'    : Disk_Backplane,
        'Interposer'        : Interposer,
        'SSD'               : SSD,
        'Power_Housing'     : Power_Housing,
        'Power_Supply'      : Power_Supply,
        'Chassis'           : Chassis,
        'CPU'               : CPU,
        'DRAM'              : DRAM,
        'Mainboard'         : Mainboard,
        'RMM4_light'        : RMM4_light,
        'SATADOM'           : SATADOM,
        'Expander_Board'    : Expander_Board,
        'Riser_Card_Left'   : Riser_Card_Left,
        'FC_HBA'            : FC_HBA,
        'Riser_Card_Right'  : Riser_Card_Right,
        'Host_Bus_Adapter'  : Host_Bus_Adapter,
        'NTB'               : NTB,
        'NVRAM'             : NVRAM,
        'FAN'               : FAN,
    })

    return render_to_response('erp/state/mtr.html', rctx)

def Pro_HA201TP_Main(request, page=1):
    per_page = 20
    start_pos = (page -1) * per_page
    end_pos = start_pos + per_page

    page_title = ''

    ha201tp_mnft = []

    try:
        ha201tp_ready  = models.HA201_TP.objects.filter()
        ha201tp_ready_cnt  = ha201tp_ready.count()
    except:
        ha201tp_ready = ha201tp_ready_cnt = 0

    #try:
    #    ha201tp_start  = models.HA201_TP.objects.filter(ha201tp_state=0, ha201tp_using=1, ha201tp_out=0)
    #    ha201tp_start_cnt  = len(ha201tp_start)
    #except:
    #    ha201tp_start = ha201tp_start_cnt = 0

    #try:
    #    ha201tp_mnft   = models.HA201TPFactoryReport.objects.select_related().all()
    #    ha201tp_mnft_cnt   = len(ha201tp_mnft)
    #except:
    #    ha201tp_mnft = ha201tp_mnft_cnt = 0

    #try:
    #    ha201tp_assign  = models.HA201TPFactoryReport.filter(ftr_complete=1)
    #    ha201tp_assign_cnt  = len(ha201tp_assign)
    #except:
    #    ha201tp_assign = ha201tp_assign_cnt = 0

    #try:
    #    ha201tp_order  = models.HA201TPOrderReport.filter(orr_complete=1)
    #    ha201tp_order_cnt  = len(ha201tp_order)
    #except:
    #    ha201tp_order = ha201tp_order = 0

    #try:
    #    ha201tp_finish = models.HA201TPDeliveryReport.filter(dlr_complete=1)
    #    ha201tp_finish_cnt = len(ha201tp_finish)
    #except:
    #    ha201tp_finish = ha201tp_finish_cnt = 0

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'ha201tp_ready'       :  ha201tp_ready,
        'ha201tp_ready_cnt'   :  ha201tp_ready_cnt,
        #'ha201tp_start'       :  ha201tp_start,
        #'ha201tp_start_cnt'   :  ha201tp_start_cnt,
        #'ha201tp_mnft'        :  ha201tp_mnft,
        #'ha201tp_mnft_cnt'    :  ha201tp_mnft_cnt,
        #'ha201tp_assign'      :  ha201tp_assign,
        #'ha201tp_asign_cnt'   :  ha201tp_asign_cnt,
        #'ha201tp_order'       :  ha201tp_order,
        #'ha201tp_order_cnt'   :  ha201tp_order_cnt,
        #'ha201tp_finish'      :  ha201tp_finish,
        #'ha201tp_finish_cnt'  :  ha201tp_finish_cnt,
    })

    return render_to_response('erp/state/pro/HA201_TP.html', rctx)

#===Read
def Cus_Read(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaCustomer.objects.get(id=int(entry_id))

    prev_entry = current_entry.get_previous_by_created()

    next_entry = current_entry.get_next_by_created()

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'prev_entry' : prev_entry,
        'next_entry' : next_entry,
        'current_entry' : current_entry,
    })

    models.GayaCustomer.objects.count()

    return render_to_response('erp/state/read/cus.html', rctx)

#===Write
def Asr01_Write(request):
    page_title = ''

    ha201tp = models.HA201_TP.objects.filter(pro_using=0, pro_out=0).order_by('-pro_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'ha201tp' : ha201tp,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/state/write/asr01.html', rctx)

def Asr02_Write(request):
    page_title = ''

    gayaasr = models.AssembleReport.objects.filter(asr_start=1, asr_complete=0, asr_out=0).order_by('-asr_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaasr' : gayaasr,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/state/write/asr02.html', rctx)

def Isr_Write(request):
    page_title = ''

    gayaasr = models.AssembleReport.objects.filter(asr_complete=1, asr_out=0, asr_add=0).order_by('-asr_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaasr' : gayaasr,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/state/write/isr.html', rctx)

def Pcr_Write(request):
    page_title = ''

    gayaisr = models.InspectionReport.objects.filter(isr_complete=1, isr_out=0, isr_add=0).order_by('-isr_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaisr' : gayaisr,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/state/write/pcr.html', rctx)

def Orr_Write(request):
    page_title = ''

    gayapcr = models.PackagingReport.objects.filter(pcr_complete=1, pcr_out=0, pcr_add=0).order_by('-pcr_created')
    gayaord = models.GayaOrder.objects.filter(ord_complete=0).order_by('-ord_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayapcr' : gayapcr,
        'gayaord' : gayaord,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/state/write/orr.html', rctx)

def Dlr_Write(request):
    page_title = ''

    gayaorr = models.OrderReport.objects.filter(orr_complete=1, orr_add=0).order_by('-orr_created')
    gayaemp = models.GayaEmp.objects.select_related().all().order_by('-emp_created')

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'gayaorr' : gayaorr,
        'gayaemp' : gayaemp,
    })
    return render_to_response('erp/state/write/dlr.html', rctx)

#===Add
@csrf_exempt
def Asr01_Add(request):
    if request.POST.has_key('asr_pid') == False:
        return HttpResponse('')
    else:
        try:
            pid = request.POST['asr_pid']
        except:
            return HttpResponse('')

# 생산시작 구분 Asr01과 Asr02
# 생산이 시작되면 HA201_TP를 [생산시작]단계로 변경
    if request.POST.has_key('asr_pro') == False:
        return HttpResponse('')
    else:
        try:
            pNum = int(request.POST['asr_pro'])
            if pNum == 0:
                ha201tp = models.HA201_TP.objects.get(id=pid)
                ha201tp.pro_using = 1# <--
                pro = 'HA201_TP'
                psn = ha201tp.pro_sn
                try:
                    ha201tp.save()
                except:
                    return HttpResponse('')
        except:
            return HttpResponse('')

    if request.POST.has_key('asr_s_emp') == False:
        return HttpResponse('')
    else:
        try:
            s_emp = models.GayaEmp.objects.get(id=request.POST['asr_s_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('asr_startday') == False:
        return HttpResponse('')
    else:
        if len(request.POST['asr_startday']) == 0:
            return HttpResponse('')
        else:
            startday = request.POST['asr_startday']

    if request.POST.has_key('asr_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['asr_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['asr_author']

    if request.POST.has_key('asr_note') == False:
        note = ''
    else:
        if len(request.POST['asr_note']) == 0:
            note = ''
        else:
            note = request.POST['asr_note']

    new_entry = models.AssembleReport(asr_pro=pro, asr_psn=psn, asr_s_emp=s_emp, asr_startday=startday, asr_start=1, asr_author=author, asr_note=note)

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/state/write/asr01.html')

@csrf_exempt
def Asr02_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('asr_id') == False:
            return HttpResponse('')
        else:
            try:
# 검색된 Report로 HA201_TP를 재검색하고 [조립완료]단계로 변경
                asr = models.AssembleReport.objects.get(id=request.POST['asr_id'])
                if asr.asr_pro == 'HA201_TP':
                    pro = models.HA201_TP.objects.get(pro_sn=asr.asr_psn)
                    pro.pro_using = 2#<--
                    try:
                        pro.save()
                    except:
                        return HttpResponse('1')
            except:
                return HttpResponse('1')

        if request.POST.has_key('asr_c_emp') == False:
            return HttpResponse('2')
        else:
            if len(request.POST['asr_c_emp']) == 0:
                return HttpResponse('2')
            else:
                c_emp = request.POST['asr_c_emp']

        if request.POST.has_key('asr_completeday') == False:
            return HttpResponse('3')
        else:
            if len(request.POST['asr_completeday']) == 0:
                return HttpResponse('3')
            else:
                completeday = request.POST['asr_completeday']

        if request.POST.has_key('asr_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['asr_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['asr_author']

        if request.POST.has_key('asr_note') == False:
            note = ''
        else:
            if len(request.POST['asr_note']) == 0:
                note = ''
            else:
                note = request.POST['asr_note']

# Report 파일이 존재하면 저장
        if 'asr_report' in request.FILES:
            chkNum = 0
            report = request.FILES['asr_report']
        else:
            chkNum = 1

    else:
        pass

    asr.asr_c_emp = c_emp
    asr.asr_completeday = completeday
    asr.asr_complete = 1
    asr.asr_author = author
    asr.asr_note = note

    if chkNum == 0:
        asr.asr_report = report

    try:
        asr.save()
    except:
        return HttpResponse('4')
    return HttpResponseRedirect('/erp/state/write/asr02.html')

@csrf_exempt
def Isr_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('isr_asr') == False:
            return HttpResponse('')
        else:
            try:
# 검색된 Report로 HA201_TP를 재검색하고 [검증완료]단계로 변경
                asr = models.AssembleReport.objects.get(id=request.POST['isr_asr'])
                if asr.asr_pro == 'HA201_TP':
                    pro = models.HA201_TP.objects.get(pro_sn=asr.asr_psn)
                    pro.pro_using = 3
                    try:
                        pro.save()
                    except:
                        return HttpResponse('')
            except:
                return HttpResponse('')

        if request.POST.has_key('isr_emp') == False:
            return HttpResponse('')
        else:
            try:
                emp = models.GayaEmp.objects.get(id=request.POST['isr_emp'])
            except:
                return HttpResponse('')

        if request.POST.has_key('isr_completeday') == False:
            return HttpResponse('')
        else:
            if len(request.POST['isr_completeday']) == 0:
                return HttpResponse('')
            else:
                completeday = request.POST['isr_completeday']

        if request.POST.has_key('isr_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['isr_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['isr_author']

        if request.POST.has_key('isr_note') == False:
            note = ''
        else:
            if len(request.POST['isr_note']) == 0:
                note = ''
            else:
                note = request.POST['isr_note']

        if 'isr_report' in request.FILES:
            chkNum = 0
            report = request.FILES['isr_report']
        else:
            chkNum = 1

    else:
        pass

    if chkNum == 0:
        new_entry = models.InspectionReport(isr_asr=asr, isr_emp=emp, isr_completeday=completeday, isr_complete=1,
                isr_author=author, isr_note=note, isr_report=report)
    else:
        new_entry = models.InspectionReport(isr_asr=asr, isr_emp=emp, isr_completeday=completeday, isr_complete=1,
                isr_author=author, isr_note=note)

# [생산시작 및 조립등록] 변경
    asr.asr_add = 1
    try:
        asr.save()
    except:
        return HttpResponse('')

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/state/write/isr.html')

@csrf_exempt
def Pcr_Add(request):
    if request.method == 'POST':
        if request.POST.has_key('pcr_isr') == False:
            return HttpResponse('')
        else:
            try:
# 검색된 Report로 HA201_TP를 재검색하고 [포장완료]단계로 변경
                isr = models.InspectionReport.objects.get(id=request.POST['pcr_isr'])
                if isr.isr_asr.asr_pro == 'HA201_TP':
                    pro = models.HA201_TP.objects.get(pro_sn=isr.isr_asr.asr_psn)
                    pro.pro_using = 4
                    try:
                        pro.save()
                    except:
                        return HttpResponse('1')
            except:
                return HttpResponse('')

        if request.POST.has_key('pcr_emp') == False:
            return HttpResponse('')
        else:
            try:
                emp = models.GayaEmp.objects.get(id=request.POST['pcr_emp'])
            except:
                return HttpResponse('')

        if request.POST.has_key('pcr_completeday') == False:
            return HttpResponse('')
        else:
            if len(request.POST['pcr_completeday']) == 0:
                return HttpResponse('')
            else:
                completeday = request.POST['pcr_completeday']

        if request.POST.has_key('pcr_author') == False:
            return HttpResponse('')
        else:
            if len(request.POST['pcr_author']) == 0:
                return HttpResponse('')
            else:
                author = request.POST['pcr_author']

        if request.POST.has_key('pcr_note') == False:
            note = ''
        else:
            if len(request.POST['pcr_note']) == 0:
                note = ''
            else:
                note = request.POST['pcr_note']

        if 'pcr_report' in request.FILES:
            chkNum = 0
            report = request.FILES['pcr_report']
        else:
            chkNum = 1

    else:
        pass

    if chkNum == 0:
        new_entry = models.PackagingReport(pcr_isr=isr, pcr_emp=emp, pcr_completeday=completeday, pcr_complete=1,
                pcr_author=author, pcr_note=note, pcr_report=report)
    else:
        new_entry = models.PackagingReport(pcr_isr=isr, pcr_emp=emp, pcr_completeday=completeday, pcr_complete=1,
                pcr_author=author, pcr_note=note)

# [검증등록] 변경
    isr.isr_add = 1
    try:
        isr.save()
    except:
        return HttpResponse('')

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/state/write/pcr.html')

@csrf_exempt
def Orr_Add(request):
    if request.POST.has_key('orr_pcr') == False:
        return HttpResponse('')
    else:
        try:
# 검색된 Report로 HA201_TP를 재검색하고 [주문할당]단계로 변경
            pcr = models.PackagingReport.objects.get(id=request.POST['orr_pcr'])
            if pcr.pcr_isr.isr_asr.asr_pro == 'HA201_TP':
                pro = models.HA201_TP.objects.get(pro_sn=pcr.pcr_isr.isr_asr.asr_psn)
                pro.pro_using = 5
                try:
                    pro.save()
                except:
                    return HttpResponse('1')
        except:
            return HttpResponse('')

    if request.POST.has_key('orr_ord') == False:
        return HttpResponse('')
    else:
        try:
            ord = models.GayaOrder.objects.get(id=request.POST['orr_ord'])
        except:
            return HttpResponse('')

    if request.POST.has_key('orr_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['orr_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('orr_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['orr_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['orr_author']

    if request.POST.has_key('orr_note') == False:
        note = ''
    else:
        if len(request.POST['orr_note']) == 0:
            note = ''
        else:
            note = request.POST['orr_note']

# [주문Report완료] 변경
    new_entry = models.OrderReport(orr_pcr=pcr, orr_ord=ord, orr_emp=emp, orr_complete=1, orr_author=author, orr_note=note)

# [포장등록][주문완료] 변경
    pcr.pcr_add = 1
    ord.ord_complete = 1
    try:
        pcr.save()
    except:
        return HttpResponse('')

    try:
        ord.save()
    except:
        return HttpResponse('')

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/state/write/orr.html')

@csrf_exempt
def Dlr_Add(request):
    if request.POST.has_key('dlr_orr') == False:
        return HttpResponse('')
    else:
        try:
            orr = models.OrderReport.objects.get(id=request.POST['dlr_orr'])
        except:
            return HttpResponse('')

    if request.POST.has_key('dlr_emp') == False:
        return HttpResponse('')
    else:
        try:
            emp = models.GayaEmp.objects.get(id=request.POST['dlr_emp'])
        except:
            return HttpResponse('')

    if request.POST.has_key('dlr_when') == False:
        return HttpResponse('')
    else:
        if len(request.POST['dlr_when']) == 0:
            return HttpResponse('')
        else:
            when = request.POST['dlr_when']

    if request.POST.has_key('dlr_where') == False:
        return HttpResponse('')
    else:
        if len(request.POST['dlr_where']) == 0:
            return HttpResponse('')
        else:
            where = request.POST['dlr_where']

    if request.POST.has_key('dlr_how') == False:
        return HttpResponse('')
    else:
        if len(request.POST['dlr_how']) == 0:
            return HttpResponse('')
        else:
            how = request.POST['dlr_how']

    if request.POST.has_key('dlr_author') == False:
        return HttpResponse('')
    else:
        if len(request.POST['dlr_author']) == 0:
            return HttpResponse('')
        else:
            author = request.POST['dlr_author']

    if request.POST.has_key('dlr_note') == False:
        note = ''
    else:
        if len(request.POST['dlr_note']) == 0:
            note = ''
        else:
            note = request.POST['dlr_note']

# [출고Report완료]
    new_entry = models.DeliveryReport(dlr_orr=orr, dlr_emp=emp, dlr_when=when, dlr_where=where, dlr_how=how,
            dlr_complete=1, dlr_author=author, dlr_note=note)

    try:
        ordInfo = models.GayaOrder.objects.get(id=int(orr.orr_ord.id))
    except:
        pass
    try:
        orrCnt = models.OrderReport.objects.filter(orr_ord=orr.orr_ord).count()
    except:
        pass
    try:
        gayapcr = models.PackagingReport.objects.get(id=int(orr.orr_pcr.id))
    except:
        pass
    try:
        gayaisr = models.InspectionReport.objects.get(id=int(gayapcr.pcr_isr.id))
    except:
        pass
    try:
        gayaasr = models.AssembleReport.objects.get(id=int(gayaisr.isr_asr.id))
    except:
        pass

    if gayaasr.asr_pro == 'HA201_TP':
        try: # [출고완료] 변경
            ha201tp = models.HA201_TP.objects.get(pro_sn=gayaasr.asr_psn)
            ha201tp.pro_out = 1
            try:
                ha201tp.save()
            except:
                return HttpResponse('')
        except:
            return HttpResponse('')

# [주문완료] 변경
    if int(ordInfo.ord_total) == orrCnt:
        ordInfo.ord_complete = 2
        try:
            ordInfo.save()
        except:
            pass

# [주문Report등록] 변경
    orr.orr_add = 1
    try:
        orr.save()
    except:
        return HttpResponse('')

# 생산Report에 [출고완료] 변경
    gayaasr.asr_out = 1
    gayaisr.isr_out = 1
    gayapcr.pcr_out = 1

    try:
        gayaasr.save()
    except:
        pass
    try:
        gayaisr.save()
    except:
        pass
    try:
        gayapcr.save()
    except:
        pass

# 할당되어 있는 자재에 [출고완료] 변경
    gayamsn = models.GayaMaterialSN.objects.filter(msn_psn=gayaasr.asr_psn)
    for msn in gayamsn:
        msn.msn_out = 1
        try:
            msn.save()
        except:
            pass

    try:
        new_entry.save()
    except:
        return HttpResponse('')
    return HttpResponseRedirect('/erp/state/write/dlr.html')

#===Mod
def Mtp_Mod(request, entry_id=None):
    page_title = ''

    current_entry = models.GayaMaterialReport.objects.get(id=int(entry_id))
    gayapsn = models.GayaProductSN.objects.filter(psn_using=1, psn_out=0)
    gayamsn = models.GayaMaterialSN.objects.filter(msn_out=0)
    gayaemp = models.GayaEmp.objects.select_related().all()

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
        'gayapsn' : gayapsn,
        'gayamsn' : gayamsn,
        'gayaemp' : gayaemp,
    })

    return render_to_response('erp/state/modify/mtp.html', rctx)

def HA201TP_Ftr_Mod(request, entry_id=None):
    page_title = ''

    current_entry = models.HA201TPFactoryReport.objects.get(id=int(entry_id))
    gayapsn = models.GayaProductSN.objects.filter(psn_using=1)
    gayaemp = models.GayaEmp.objects.select_related().all()

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
        'gayapsn' : gayapsn,
        'gayaemp' : gayaemp,
    })

    return render_to_response('erp/state/modify/ftr.html', rctx)

def Orr_Mod(request, entry_id=None):
    page_title = ''

    current_entry = models.OrderReport.objects.get(id=int(entry_id))
    pro_pcr = models.PackagingReport.objects.filter(ftr_complete=1)
    gayaord = models.GayaOrder.objects.filter(ord_complete=0)
    gayaemp = models.GayaEmp.objects.select_related().all()

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
        'pro_ftr' : pro_ftr,
        'gayaord' : gayaord,
        'gayaemp' : gayaemp,
    })

    return render_to_response('erp/state/modify/orr.html', rctx)

def Dlr_Mod(request, entry_id=None):
    page_title = ''

    current_entry = models.DeliveryReport.objects.get(id=int(entry_id))
    pro_orr = models.OrderReport.objects.filter(orr_complete=1)
    gayaemp = models.GayaEmp.objects.select_related().all()

    rctx = RequestContext(request, {
        'page_title' : page_title,
        'current_entry' : current_entry,
        'pro_orr' : pro_orr,
        'gayaemp' : gayaemp,
    })

    return render_to_response('erp/state/modify/dlr.html', rctx)

