#-*- coding: utf-8 -*-

from django.conf.urls import patterns, url
from erp import views
from erp import stateviews
from erp import mgmtviews
from erp import supportviews
from erp import socialviews


# url(매칭될 url, 사용될 함수, 사용될 이름)
urlpatterns = patterns('',
    url(r'^index.html$'                  , views.Gaya_Main                , name='gaya_main'          ),#
    url(r'^about.html$'                  , views.Gaya_About               , name='gaya_about'         ),#

    url(r'^state/main.html$'             , stateviews.State_Main          , name='state_main'         ),#
    url(r'^state/ord.html$'              , stateviews.Ord_Main            , name='ord_main'           ),#
    url(r'^state/pro.html$'              , stateviews.Pro_Main            , name='pro_main'           ),#
    url(r'^state/pro/HA201_TP.html$'     , stateviews.Pro_HA201TP_Main    , name='pro_ha201tp_main'   ),#
    url(r'^state/mtr.html$'              , stateviews.Mtr_Main            , name='mtr_main'           ),#

    url(r'^mgmt/main.html$'              , mgmtviews.Mgmt_Main            , name='mgmt_main'          ),#
    url(r'^mgmt/emp.html$'               , mgmtviews.Emp_Main             , name='emp_main'           ),#
    url(r'^mgmt/cus.html$'               , mgmtviews.Cus_Main             , name='cus_main'           ),#
    url(r'^mgmt/pro.html$'               , mgmtviews.Pro_Main             , name='pro_main'           ),#
    url(r'^mgmt/HA201_TP.html$'          , mgmtviews.HA201TP_Main         , name='ha201tp_main'       ),#
    url(r'^mgmt/mtr.html$'               , mgmtviews.Mtr_Main             , name='mtr_main'           ),#
    url(r'^mgmt/ord.html$'               , mgmtviews.Ord_Main             , name='ord_main'           ),#
    url(r'^mgmt/msn.html$'               , mgmtviews.Msn_Main             , name='msn_main'           ),#

    url(r'^mgmt/mtr/(?P<page>\d+)/$'     , mgmtviews.Mtr_Main             , name='mtr_main'           ),#
    url(r'^mgmt/msn/(?P<page>\d+)/$'     , mgmtviews.Msn_Main             , name='msn_main'           ),#

    url(r'^support/main.html$'           , supportviews.Support_Main      , name='support_main'       ),#
    url(r'^support/stl.html$'            , supportviews.Stl_Main          , name='stl_main'           ),#
    url(r'^support/stw.html$'            , supportviews.Stw_Main          , name='stw_main'           ),#
    url(r'^support/stv.html$'            , supportviews.Stv_Main          , name='stv_main'           ),#
    url(r'^support/stt.html$'            , supportviews.Stt_Main          , name='stt_main'           ),#
    url(r'^support/stc.html$'            , supportviews.Stc_Main          , name='stc_main'           ),#
    url(r'^support/std.html$'            , supportviews.Std_Main          , name='std_main'           ),#

    url(r'^social/main.html$'            , socialviews.Social_Main        , name='social_main'        ),#
    url(r'^social/scc.html$'             , socialviews.Scc_Main           , name='scc_main'           ),#
    url(r'^social/scf.html$'             , socialviews.Scf_Main           , name='scf_main'           ),#
    url(r'^social/scr.html$'             , socialviews.Scr_Main           , name='scr_main'           ),#
    url(r'^social/scq.html$'             , socialviews.Scq_Main           , name='scq_main'           ),#

    url(r'^mgmt/read/emp_read/(?P<entry_id>\d+)/$'         , mgmtviews.Emp_Read          , name='emp_read'          ),#
    url(r'^mgmt/read/cus_read/(?P<entry_id>\d+)/$'         , mgmtviews.Cus_Read          , name='cus_read'          ),#
    url(r'^mgmt/read/pro_read/(?P<entry_id>\d+)/$'         , mgmtviews.Pro_Read          , name='pro_read'          ),#
    url(r'^mgmt/read/ha201_tp_read/(?P<entry_id>\d+)/$'    , mgmtviews.HA201TP_Read      , name='ha201tp_read'      ),#
    url(r'^mgmt/read/mtr_read/(?P<entry_id>\d+)/$'         , mgmtviews.Mtr_Read          , name='mtr_read'          ),#
    url(r'^mgmt/read/ord_read/(?P<entry_id>\d+)/$'         , mgmtviews.Ord_Read          , name='ord_read'          ),#
    url(r'^mgmt/read/msn_read/(?P<entry_id>\d+)/$'         , mgmtviews.Msn_Read          , name='msn_read'          ),#

    url(r'^support/read/stl_read/(?P<entry_id>\d+)$'       , supportviews.Stl_Read       , name='stl_read'          ),#
    url(r'^support/read/stw_read/(?P<entry_id>\d+)$'       , supportviews.Stw_Read       , name='stw_read'          ),#
    url(r'^support/read/stv_read/(?P<entry_id>\d+)$'       , supportviews.Stv_Read       , name='stv_read'          ),#
    url(r'^support/read/stt_read/(?P<entry_id>\d+)$'       , supportviews.Stt_Read       , name='stt_read'          ),#
    url(r'^support/read/stc_read/(?P<entry_id>\d+)$'       , supportviews.Stc_Read       , name='stc_read'          ),#
    url(r'^support/read/std_read/(?P<entry_id>\d+)$'       , supportviews.Std_Read       , name='std_read'          ),#

    url(r'^social/read/scc_read/(?P<entry_id>\d+)$'        , socialviews.Scc_Read        , name='scc_read'          ),#
    url(r'^social/read/scf_read/(?P<entry_id>\d+)$'        , socialviews.Scf_Read        , name='scf_read'          ),#
    url(r'^social/read/scr_read/(?P<entry_id>\d+)$'        , socialviews.Scr_Read        , name='scr_read'          ),#
    url(r'^social/read/scq_read/(?P<entry_id>\d+)$'        , socialviews.Scq_Read        , name='scq_read'          ),#

    #url(r'^state/write/ftr01.html$'      , stateviews.HA201TP_Ftr01_Write  , name='ha201tp_ftr01_write'  ),#
    #url(r'^state/write/ftr02.html$'      , stateviews.HA201TP_Ftr02_Write  , name='ha201tp_ftr02_write'  ),#
    #url(r'^state/write/ftr03.html$'      , stateviews.HA201TP_Ftr03_Write  , name='ha201tp_ftr03_write'  ),#
    url(r'^state/write/asr01.html$'      , stateviews.Asr01_Write          , name='asr01_write'          ),#
    url(r'^state/write/asr02.html$'      , stateviews.Asr02_Write          , name='asr02_write'          ),#
    url(r'^state/write/isr.html$'        , stateviews.Isr_Write            , name='isr_write'            ),#
    url(r'^state/write/pcr.html$'        , stateviews.Pcr_Write            , name='pcr_write'            ),#
    url(r'^state/write/orr.html$'        , stateviews.Orr_Write            , name='orr_write'            ),#
    url(r'^state/write/dlr.html$'        , stateviews.Dlr_Write            , name='dlr_write'            ),#

    url(r'^mgmt/write/emp.html$'         , mgmtviews.Emp_Write             , name='emp_write'            ),#
    url(r'^mgmt/write/cus.html$'         , mgmtviews.Cus_Write             , name='cus_write'            ),#
    url(r'^mgmt/write/pro.html$'         , mgmtviews.Pro_Write             , name='pro_write'            ),#
    url(r'^mgmt/write/ha201_tp.html$'    , mgmtviews.HA201TP_Write         , name='ha201tp_write'        ),#
    url(r'^mgmt/write/mtr.html$'         , mgmtviews.Mtr_Write             , name='mtr_write'            ),#
    url(r'^mgmt/write/ord.html$'         , mgmtviews.Ord_Write             , name='ord_write'            ),#
    url(r'^mgmt/write/msn.html$'         , mgmtviews.Msn_Write             , name='msn_write'            ),#

    url(r'^support/write/stl.html$'      , supportviews.Stl_Write          , name='stl_write'            ),#
    url(r'^support/write/stw.html$'      , supportviews.Stw_Write          , name='stw_write'            ),#
    url(r'^support/write/stv.html$'      , supportviews.Stv_Write          , name='stv_write'            ),#
    url(r'^support/write/stt.html$'      , supportviews.Stt_Write          , name='stt_write'            ),#
    url(r'^support/write/stc.html$'      , supportviews.Stc_Write          , name='stc_write'            ),#
    url(r'^support/write/std.html$'      , supportviews.Std_Write          , name='std_write'            ),#

    url(r'^social/write/scc.html$'       , socialviews.Scc_Write           , name='scc_write'            ),#
    url(r'^social/write/scf.html$'       , socialviews.Scf_Write           , name='scf_write'            ),#
    url(r'^social/write/scr.html$'       , socialviews.Scr_Write           , name='scr_write'            ),#
    url(r'^social/write/scq.html$'       , socialviews.Scq_Write           , name='scq_write'            ),#

    #url(r'^state/add/ftr01/$'      , stateviews.HA201TP_Ftr01_Add  , name='ha201tp_ftr01_add'   ),#
    #url(r'^state/add/ftr02/$'      , stateviews.HA201TP_Ftr02_Add  , name='ha201tp_ftr02_add'   ),#
    #url(r'^state/add/ftr03/$'      , stateviews.HA201TP_Ftr03_Add  , name='ha201tp_ftr03_add'   ),#
    url(r'^state/add/asr01/$'      , stateviews.Asr01_Add  , name='asr01_add'   ),#
    url(r'^state/add/asr02/$'      , stateviews.Asr02_Add  , name='asr02_add'   ),#
    url(r'^state/add/isr/$'        , stateviews.Isr_Add    , name='isr_add'     ),#
    url(r'^state/add/pcr/$'        , stateviews.Pcr_Add    , name='pcr_add'     ),#
    url(r'^state/add/orr/$'        , stateviews.Orr_Add    , name='orr_add'     ),#
    url(r'^state/add/dlr/$'        , stateviews.Dlr_Add    , name='dlr_add'     ),#

    url(r'^mgmt/add/emp/$'         , mgmtviews.Emp_Add             , name='emp_add'             ),#
    url(r'^mgmt/add/cus/$'         , mgmtviews.Cus_Add             , name='cus_add'             ),#
    url(r'^mgmt/add/pro/$'         , mgmtviews.Pro_Add             , name='pro_add'             ),#
    url(r'^mgmt/add/ha201_tp/$'    , mgmtviews.HA201TP_Add         , name='ha201tp_add'         ),#
    url(r'^mgmt/add/mtr/$'         , mgmtviews.Mtr_Add             , name='mtr_add'             ),#
    url(r'^mgmt/add/ord/$'         , mgmtviews.Ord_Add             , name='ord_add'             ),#
    url(r'^mgmt/add/msn/$'         , mgmtviews.Msn_Add             , name='msn_add'             ),#

    url(r'^support/add/stl/$'      , supportviews.Stl_Add          , name='stl_add'             ),#
    url(r'^support/add/stw/$'      , supportviews.Stw_Add          , name='stw_add'             ),#
    url(r'^support/add/stv/$'      , supportviews.Stv_Add          , name='stv_add'             ),#
    url(r'^support/add/stt/$'      , supportviews.Stt_Add          , name='stt_add'             ),#
    url(r'^support/add/stc/$'      , supportviews.Stc_Add          , name='stc_add'             ),#
    url(r'^support/add/std/$'      , supportviews.Std_Add          , name='std_add'             ),#

    url(r'^social/add/scc/$'       , socialviews.Scc_Add           , name='scc_add'             ),#
    url(r'^social/add/scf/$'       , socialviews.Scf_Add           , name='scf_add'             ),#
    url(r'^social/add/scr/$'       , socialviews.Scr_Add           , name='scr_add'             ),#
    url(r'^social/add/scq/$'       , socialviews.Scq_Add           , name='scq_add'             ),#

    url(r'^support/add/stl_comadd/$'      , supportviews.Stc_Comadd      , name='stl_comadd'    ),#
    url(r'^support/add/stw_comadd/$'      , supportviews.Stw_Comadd      , name='stw_comadd'    ),#
    url(r'^support/add/stv_comadd/$'      , supportviews.Stv_Comadd      , name='stv_comadd'    ),#
    url(r'^support/add/stt_comadd/$'      , supportviews.Stt_Comadd      , name='stt_comadd'    ),#
    url(r'^support/add/stc_comadd/$'      , supportviews.Stc_Comadd      , name='stc_comadd'    ),#
    url(r'^support/add/std_comadd/$'      , supportviews.Std_Comadd      , name='std_comadd'    ),#

    url(r'^social/add/scc_comadd/$'       , socialviews.Scc_Comadd       , name='scc_comadd'    ),#
    url(r'^social/add/scf_comadd/$'       , socialviews.Scf_Comadd       , name='scf_comadd'    ),#
    url(r'^social/add/scr_comadd/$'       , socialviews.Scr_Comadd       , name='scr_comadd'    ),#
    url(r'^social/add/scq_comadd/$'       , socialviews.Scq_Comadd       , name='scq_comadd'    ),#

    #url(r'^state/modify/ftr_mod/(?P<entry_id>\d+)$'         , stateviews.HA201TP_Ftr_Mod    , name='ha201tp_ftr_mod'     ),#
    #url(r'^state/modify/orr_mod/(?P<entry_id>\d+)$'         , stateviews.HA201TP_Orr_Mod    , name='ha201tp_orr_mod'     ),#
    #url(r'^state/modify/dlr_mod/(?P<entry_id>\d+)$'         , stateviews.HA201TP_Dlr_Mod    , name='ha201tp_dlr_mod'     ),#

    url(r'^mgmt/modify/emp_mod/(?P<entry_id>\d+)/$'         , mgmtviews.Emp_Mod             , name='emp_mod'             ),#
    url(r'^mgmt/modify/cus_mod/(?P<entry_id>\d+)/$'         , mgmtviews.Cus_Mod             , name='cus_mod'             ),#
    url(r'^mgmt/modify/pro_mod/(?P<entry_id>\d+)/$'         , mgmtviews.Pro_Mod             , name='pro_mod'             ),#
    url(r'^mgmt/modify/ha201_tp_mod/(?P<entry_id>\d+)/$'    , mgmtviews.HA201TP_Mod         , name='ha201tp_mod'         ),#
    url(r'^mgmt/modify/mtr_mod/(?P<entry_id>\d+)/$'         , mgmtviews.Mtr_Mod             , name='mtr_mod'             ),#
    url(r'^mgmt/modify/ord_mod/(?P<entry_id>\d+)/$'         , mgmtviews.Ord_Mod             , name='ord_mod'             ),#
    url(r'^mgmt/modify/msn_mod/(?P<entry_id>\d+)/$'         , mgmtviews.Msn_Mod             , name='msn_mod'             ),#

    url(r'^support/modify/stl_mod/(?P<entry_id>\d+)$'       , supportviews.Stl_Mod          , name='stl_mod'             ),#
    url(r'^support/modify/stw_mod/(?P<entry_id>\d+)$'       , supportviews.Stw_Mod          , name='stw_mod'             ),#
    url(r'^support/modify/stv_mod/(?P<entry_id>\d+)$'       , supportviews.Stv_Mod          , name='stv_mod'             ),#
    url(r'^support/modify/stt_mod/(?P<entry_id>\d+)$'       , supportviews.Stt_Mod          , name='stt_mod'             ),#
    url(r'^support/modify/stc_mod/(?P<entry_id>\d+)$'       , supportviews.Stc_Mod          , name='stc_mod'             ),#
    url(r'^support/modify/std_mod/(?P<entry_id>\d+)$'       , supportviews.Std_Mod          , name='std_mod'             ),#

    url(r'^social/modify/scc_mod/(?P<entry_id>\d+)$'        , socialviews.Scc_Mod           , name='scc_mod'             ),#
    url(r'^social/modify/scf_mod/(?P<entry_id>\d+)$'        , socialviews.Scf_Mod           , name='scf_mod'             ),#
    url(r'^social/modify/scr_mod/(?P<entry_id>\d+)$'        , socialviews.Scr_Mod           , name='scr_mod'             ),#
    url(r'^social/modify/scq_mod/(?P<entry_id>\d+)$'        , socialviews.Scq_Mod           , name='scq_mod'             ),#

    url(r'^mgmt/delete/emp_del/(?P<entry_id>\d+)/$'         , mgmtviews.Emp_Del             , name='emp_del'             ),#
    url(r'^mgmt/delete/cus_del/(?P<entry_id>\d+)/$'         , mgmtviews.Cus_Del             , name='cus_del'             ),#
    url(r'^mgmt/delete/pro_del/(?P<entry_id>\d+)/$'         , mgmtviews.Pro_Del             , name='pro_del'             ),#
    url(r'^mgmt/delete/ha201_tp_del/(?P<entry_id>\d+)/$'    , mgmtviews.HA201TP_Del         , name='ha201tp_del'         ),#
    url(r'^mgmt/delete/mtr_del/(?P<entry_id>\d+)/$'         , mgmtviews.Mtr_Del             , name='mtr_del'             ),#
    url(r'^mgmt/delete/ord_del/(?P<entry_id>\d+)/$'         , mgmtviews.Ord_Del             , name='ord_del'             ),#
    url(r'^mgmt/delete/msn_del/(?P<entry_id>\d+)/$'         , mgmtviews.Msn_Del             , name='msn_del'             ),#

    url(r'^support/delete/stl_del/(?P<entry_id>\d+)$'       , supportviews.Stl_Del          , name='stl_del'             ),#
    url(r'^support/delete/stw_del/(?P<entry_id>\d+)$'       , supportviews.Stw_Del          , name='stw_del'             ),#
    url(r'^support/delete/stv_del/(?P<entry_id>\d+)$'       , supportviews.Stv_Del          , name='stv_del'             ),#
    url(r'^support/delete/stt_del/(?P<entry_id>\d+)$'       , supportviews.Stt_Del          , name='stt_del'             ),#
    url(r'^support/delete/stc_del/(?P<entry_id>\d+)$'       , supportviews.Stc_Del          , name='stc_del'             ),#
    url(r'^support/delete/std_del/(?P<entry_id>\d+)$'       , supportviews.Std_Del          , name='std_del'             ),#

    url(r'^social/delete/scc_del/(?P<entry_id>\d+)$'        , socialviews.Scc_Del           , name='scc_del'             ),#
    url(r'^social/delete/scf_del/(?P<entry_id>\d+)$'        , socialviews.Scf_Del           , name='scf_del'             ),#
    url(r'^social/delete/scr_del/(?P<entry_id>\d+)$'        , socialviews.Scr_Del           , name='scr_del'             ),#
    url(r'^social/delete/scq_del/(?P<entry_id>\d+)$'        , socialviews.Scq_Del           , name='scq_del'             ),#
)
