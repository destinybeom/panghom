#-*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# Create your models here.

# User 테이블과 통합 django 홈페이지 참고
class GayaEmpManager(BaseUserManager):
    def create_user(self, emp_email, emp_name, emp_rank, emp_phone, emp_address, emp_job, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not emp_email:
            raise ValueError('Users must have an email address')

        user = self.model(
            emp_email     = self.normalize_email(emp_email),
            emp_name      = emp_name,
            emp_rank      = emp_rank,
            emp_phone     = emp_phone,
            emp_address   = emp_address,
            emp_job       = emp_job,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, emp_email, emp_name, emp_rank, emp_phone, emp_address, emp_job, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(emp_email,
            password      = password,
            emp_name      = emp_name,
            emp_rank      = emp_rank,
            emp_phone     = emp_phone,
            emp_address   = emp_address,
            emp_job       = emp_job,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class GayaEmp(AbstractBaseUser):
    emp_email                    = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    emp_name                     = models.CharField(max_length=128)
    emp_rank                     = models.CharField(max_length=128)
    emp_phone                    = models.CharField(max_length=128)
    emp_address                  = models.CharField(max_length=255)
    emp_job                      = models.CharField(max_length=255)
    emp_pwon                     = models.IntegerField(default=0, null=True, blank=True)
    emp_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    emp_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    emp_note                     = models.TextField(null=True, blank=True)
    emp_comments                 = models.PositiveSmallIntegerField(default=0, null=True)
    is_active                    = models.BooleanField(default=True)
    is_admin                     = models.BooleanField(default=False)

    objects = GayaEmpManager()

    USERNAME_FIELD = 'emp_email'
    REQUIRED_FIELDS = ['emp_name', 'emp_rank', 'emp_phone', 'emp_address', 'emp_job',]

    def get_full_name(self):
        # The user is identified by their email address
        return self.emp_email

    def get_short_name(self):
        # The user is identified by their email address
        return self.emp_email

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5},{6}".format(
                self.emp_name
                , self.emp_rank
                , self.emp_phone
                , self.emp_email
                , self.emp_address
                , self.emp_job
                , self.emp_pwon
            )

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

class GayaCustomer(models.Model):
    cus_name                     = models.CharField(max_length=128)
    cus_section                  = models.CharField(max_length=128)
    cus_rsps                     = models.CharField(max_length=128)
    cus_rank                     = models.CharField(max_length=128)
    cus_department               = models.CharField(max_length=128)
    cus_phone                    = models.CharField(max_length=128)
    cus_rphone                   = models.CharField(max_length=128)
    cus_email                    = models.CharField(max_length=128)
    cus_address                  = models.CharField(max_length=255)
    cus_emp                      = models.ForeignKey('GayaEmp')
    cus_author                   = models.CharField(max_length=128)
    cus_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    cus_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    cus_note                     = models.TextField(null=True, blank=True)
    cus_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}".format(
                self.cus_name
                , self.cus_section
                , self.cus_rsps
                , self.cus_rank
                , self.cus_department
                , self.cus_phone
                , self.cus_rphone
                , self.cus_email
                , self.cus_address
                , self.cus_emp
            )

class GayaProductInfo(models.Model):
    pro_class                    = models.CharField(max_length=128)
    pro_name                     = models.CharField(max_length=255)
    pro_info                     = models.TextField()
    pro_emp                      = models.ForeignKey('GayaEmp')
    pro_author                   = models.CharField(max_length=128)
    pro_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    pro_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2},{3}".format(
                self.pro_class
                , self.pro_name
                , self.pro_info
                , self.pro_emp
            )

class GayaOrder(models.Model):
    ord_title                    = models.CharField(max_length=255)
    ord_ponum                    = models.CharField(max_length=128)
    ord_pro                      = models.ForeignKey('GayaProductInfo')
    ord_cus                      = models.ForeignKey('GayaCustomer')
    ord_emp                      = models.ForeignKey('GayaEmp')
    ord_total                    = models.IntegerField()
    ord_os                       = models.CharField(max_length=128, null=True, blank=True)
    ord_orderday                 = models.DateField()
    ord_delivery                 = models.DateField()
    ord_warranty                 = models.DateField()
    ord_complete                 = models.IntegerField(default=0, null=True)
    ord_author                   = models.CharField(max_length=128)
    ord_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    ord_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    ord_note                     = models.TextField(null=True, blank=True)
    ord_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format(
                self.ord_title
                , self.ord_ponum
                , self.ord_pro
                , self.ord_cus
                , self.ord_emp
                , self.ord_total
                , self.ord_os
                , self.ord_orderday
                , self.ord_delivery
                , self.ord_warranty
                , self.ord_complete
            )

class GayaMaterialInfo(models.Model):
    mtr_class                    = models.CharField(max_length=128)
    mtr_name                     = models.CharField(max_length=128)
    mtr_desc                     = models.TextField(null=True)
    mtr_total                    = models.IntegerField()
    mtr_maker                    = models.CharField(max_length=128)
    mtr_purchase                 = models.CharField(max_length=128)
    mtr_purchaseday              = models.DateField()
    mtr_repository               = models.CharField(max_length=128)
    mtr_emp                      = models.ForeignKey('GayaEmp')
    mtr_finished_sn              = models.IntegerField(default=0, null=True, blank=True)
    mtr_author                   = models.CharField(max_length=128)
    mtr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    mtr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    mtr_note                     = models.TextField(null=True, blank=True)
    mtr_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}".format(
                self.mtr_class
                , self.mtr_name
                , self.mtr_desc
                , self.mtr_total
                , self.mtr_maker
                , self.mtr_purchase
                , self.mtr_purchaseday
                , self.mtr_repository
                , self.mtr_emp
                , self.mtr_finished_sn
            )

class GayaMaterialSN(models.Model):
    msn_mtr                      = models.ForeignKey('GayaMaterialInfo')
    msn_class                    = models.CharField(max_length=128)
    msn_emp                      = models.ForeignKey('GayaEmp')
    msn_pn                       = models.CharField(max_length=128)
    msn_sn                       = models.CharField(max_length=128, unique=True)
    msn_pro                      = models.CharField(max_length=128, null=True, blank=True)
    msn_psn                      = models.CharField(max_length=128, null=True, blank=True)
    msn_state                    = models.IntegerField(default=0, null=True, blank=True)
    msn_pson                     = models.IntegerField(default=0, null=True, blank=True)
    msn_using                    = models.IntegerField(default=0, null=True, blank=True)
    msn_out                      = models.IntegerField(default=0, null=True, blank=True)
    msn_author                   = models.CharField(max_length=128)
    msn_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    msn_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    msn_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7},{8},{9}".format(
                self.msn_mtr
                , self.msn_emp
                , self.msn_pn
                , self.msn_sn
                , self.msn_pro
                , self.msn_psn
                , self.msn_state
                , self.msn_pson
                , self.msn_using
                , self.msn_out
            )

class HA201_TP(models.Model):
    pro_name                 = models.CharField(max_length=128)
    pro_class                = models.CharField(max_length=128)
    pro_pn                   = models.CharField(max_length=128)
    pro_sn                   = models.CharField(max_length=128, unique=True)
    pro_emp                  = models.ForeignKey('GayaEmp')
    pro_state                = models.IntegerField(default=0, null=True, blank=True)
    pro_using                = models.IntegerField(default=0, null=True, blank=True)
    pro_out                  = models.IntegerField(default=0, null=True, blank=True)
    pro_author               = models.CharField(max_length=128)
    pro_created              = models.DateTimeField(auto_now_add=True, auto_now=False)
    pro_modified             = models.DateTimeField(auto_now_add=False, auto_now=True)
    pro_note                 = models.TextField(null=True, blank=True)
    pro_comments             = models.PositiveSmallIntegerField(default=0, null=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5},{6},{7}".format(
                self.pro_name
                , self.pro_class
                , self.pro_pn
                , self.pro_sn
                , self.pro_emp
                , self.pro_state
                , self.pro_using
                , self.pro_out
            )

class AssembleReport(models.Model):
    asr_psn                      = models.CharField(max_length=128)
    asr_pro                      = models.CharField(max_length=128)
    asr_startday                 = models.DateField()
    asr_s_emp                    = models.ForeignKey('GayaEmp')
    asr_start                    = models.IntegerField(default=0, null=True, blank=True)
    asr_completeday              = models.DateField(null=True, blank=True)
    asr_c_emp                    = models.CharField(max_length=128, null=True, blank=True)
    asr_complete                 = models.IntegerField(default=0, null=True, blank=True)
    asr_add                      = models.IntegerField(default=0, null=True, blank=True)
    asr_report                   = models.FileField(upload_to='asr/file/%Y/%m/%d', null=True, blank=True)
    asr_out                      = models.IntegerField(default=0, null=True, blank=True)
    asr_author                   = models.CharField(max_length=128)
    asr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    asr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    asr_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4},{5}".format(
                self.asr_psn
                , self.asr_pro
                , self.asr_startday
                , self.asr_s_emp
                , self.asr_completeday
                , self.asr_c_emp
            )

class InspectionReport(models.Model):
    isr_asr                      = models.ForeignKey('AssembleReport')
    isr_completeday              = models.DateField(null=True, blank=True)
    isr_emp                      = models.ForeignKey('GayaEmp')
    isr_complete                 = models.IntegerField(default=0, null=True, blank=True)
    isr_add                      = models.IntegerField(default=0, null=True, blank=True)
    isr_report                   = models.FileField(upload_to='isr/file/%Y/%m/%d', null=True, blank=True)
    isr_out                      = models.IntegerField(default=0, null=True, blank=True)
    isr_author                   = models.CharField(max_length=128)
    isr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    isr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    isr_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2}".format(
                self.isr_asr
                , self.isr_completeday
                , self.isr_emp
            )

class PackagingReport(models.Model):
    pcr_isr                      = models.ForeignKey('InspectionReport')
    pcr_completeday              = models.DateField(null=True, blank=True)
    pcr_emp                      = models.ForeignKey('GayaEmp')
    pcr_complete                 = models.IntegerField(default=0, null=True, blank=True)
    pcr_add                      = models.IntegerField(default=0, null=True, blank=True)
    pcr_report                   = models.FileField(upload_to='pcr/file/%Y/%m/%d', null=True, blank=True)
    pcr_out                      = models.IntegerField(default=0, null=True, blank=True)
    pcr_author                   = models.CharField(max_length=128)
    pcr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    pcr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    pcr_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2}".format(
                self.pcr_isr
                , self.pcr_completeday
                , self.pcr_emp
            )

class OrderReport(models.Model):
    orr_pcr                      = models.ForeignKey('PackagingReport')
    orr_ord                      = models.ForeignKey('GayaOrder')
    orr_emp                      = models.ForeignKey('GayaEmp')
    orr_complete                 = models.IntegerField(default=0,null=True, blank=True)
    orr_add                      = models.IntegerField(default=0,null=True, blank=True)
    orr_author                   = models.CharField(max_length=128)
    orr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    orr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    orr_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2}".format(
                self.orr_pcr
                , self.orr_ord
                , self.orr_emp
            )

class DeliveryReport(models.Model):
    dlr_orr                      = models.ForeignKey('OrderReport')
    dlr_when                     = models.DateField()
    dlr_emp                      = models.ForeignKey('GayaEmp')
    dlr_where                    = models.CharField(max_length=128)
    dlr_how                      = models.CharField(max_length=128)
    dlr_complete                 = models.IntegerField(default=0,null=True, blank=True)
    dlr_add                      = models.IntegerField(default=0,null=True, blank=True)
    dlr_author                   = models.CharField(max_length=128)
    dlr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    dlr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    dlr_note                     = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "{0},{1},{2},{3},{4}".format(
                self.dlr_orr
                , self.dlr_when
                , self.dlr_emp
                , self.dlr_where
                , self.dlr_how
            )

class GayaSptLinux(models.Model):
    stl_title                    = models.CharField(max_length=255)
    stl_name                     = models.CharField(max_length=128)
    stl_pw                       = models.CharField(max_length=128)
    stl_contents                 = models.TextField()
    stl_author                   = models.CharField(max_length=128)
    stl_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    stl_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    stl_file01                   = models.FileField(upload_to='stl/file/%Y/%m/%d', null=True, blank=True)
    stl_file02                   = models.FileField(upload_to='stl/file/%Y/%m/%d', null=True, blank=True)
    stl_file03                   = models.FileField(upload_to='stl/file/%Y/%m/%d', null=True, blank=True)
    stl_file04                   = models.FileField(upload_to='stl/file/%Y/%m/%d', null=True, blank=True)
    stl_file05                   = models.FileField(upload_to='stl/file/%Y/%m/%d', null=True, blank=True)
    stl_img01                    = models.ImageField(upload_to='stl/img/%Y/%m/%d', null=True, blank=True)
    stl_img02                    = models.ImageField(upload_to='stl/img/%Y/%m/%d', null=True, blank=True)
    stl_img03                    = models.ImageField(upload_to='stl/img/%Y/%m/%d', null=True, blank=True)
    stl_img04                    = models.ImageField(upload_to='stl/img/%Y/%m/%d', null=True, blank=True)
    stl_img05                    = models.ImageField(upload_to='stl/img/%Y/%m/%d', null=True, blank=True)
    stl_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSptWindows(models.Model):
    stw_title                    = models.CharField(max_length=255)
    stw_name                     = models.CharField(max_length=128)
    stw_pw                       = models.CharField(max_length=128)
    stw_contents                 = models.TextField()
    stw_author                   = models.CharField(max_length=128)
    stw_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    stw_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    stw_file01                   = models.FileField(upload_to='stw/file/%Y/%m/%d', null=True, blank=True)
    stw_file02                   = models.FileField(upload_to='stw/file/%Y/%m/%d', null=True, blank=True)
    stw_file03                   = models.FileField(upload_to='stw/file/%Y/%m/%d', null=True, blank=True)
    stw_file04                   = models.FileField(upload_to='stw/file/%Y/%m/%d', null=True, blank=True)
    stw_file05                   = models.FileField(upload_to='stw/file/%Y/%m/%d', null=True, blank=True)
    stw_img01                    = models.ImageField(upload_to='stw/img/%Y/%m/%d', null=True, blank=True)
    stw_img02                    = models.ImageField(upload_to='stw/img/%Y/%m/%d', null=True, blank=True)
    stw_img03                    = models.ImageField(upload_to='stw/img/%Y/%m/%d', null=True, blank=True)
    stw_img04                    = models.ImageField(upload_to='stw/img/%Y/%m/%d', null=True, blank=True)
    stw_img05                    = models.ImageField(upload_to='stw/img/%Y/%m/%d', null=True, blank=True)
    stw_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSptServer(models.Model):
    stv_title                    = models.CharField(max_length=255)
    stv_name                     = models.CharField(max_length=128)
    stv_pw                       = models.CharField(max_length=128)
    stv_contents                 = models.TextField()
    stv_author                   = models.CharField(max_length=128)
    stv_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    stv_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    stv_file01                   = models.FileField(upload_to='stv/file/%Y/%m/%d', null=True, blank=True)
    stv_file02                   = models.FileField(upload_to='stv/file/%Y/%m/%d', null=True, blank=True)
    stv_file03                   = models.FileField(upload_to='stv/file/%Y/%m/%d', null=True, blank=True)
    stv_file04                   = models.FileField(upload_to='stv/file/%Y/%m/%d', null=True, blank=True)
    stv_file05                   = models.FileField(upload_to='stv/file/%Y/%m/%d', null=True, blank=True)
    stv_img01                    = models.ImageField(upload_to='stv/img/%Y/%m/%d', null=True, blank=True)
    stv_img02                    = models.ImageField(upload_to='stv/img/%Y/%m/%d', null=True, blank=True)
    stv_img03                    = models.ImageField(upload_to='stv/img/%Y/%m/%d', null=True, blank=True)
    stv_img04                    = models.ImageField(upload_to='stv/img/%Y/%m/%d', null=True, blank=True)
    stv_img05                    = models.ImageField(upload_to='stv/img/%Y/%m/%d', null=True, blank=True)
    stv_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSptStorage(models.Model):
    stt_title                    = models.CharField(max_length=255)
    stt_name                     = models.CharField(max_length=128)
    stt_pw                       = models.CharField(max_length=128)
    stt_contents                 = models.TextField()
    stt_author                   = models.CharField(max_length=128)
    stt_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    stt_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    stt_file01                   = models.FileField(upload_to='stt/file/%Y/%m/%d', null=True, blank=True)
    stt_file02                   = models.FileField(upload_to='stt/file/%Y/%m/%d', null=True, blank=True)
    stt_file03                   = models.FileField(upload_to='stt/file/%Y/%m/%d', null=True, blank=True)
    stt_file04                   = models.FileField(upload_to='stt/file/%Y/%m/%d', null=True, blank=True)
    stt_file05                   = models.FileField(upload_to='stt/file/%Y/%m/%d', null=True, blank=True)
    stt_img01                    = models.ImageField(upload_to='stt/img/%Y/%m/%d', null=True, blank=True)
    stt_img02                    = models.ImageField(upload_to='stt/img/%Y/%m/%d', null=True, blank=True)
    stt_img03                    = models.ImageField(upload_to='stt/img/%Y/%m/%d', null=True, blank=True)
    stt_img04                    = models.ImageField(upload_to='stt/img/%Y/%m/%d', null=True, blank=True)
    stt_img05                    = models.ImageField(upload_to='stt/img/%Y/%m/%d', null=True, blank=True)
    stt_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSptSwitch(models.Model):
    stc_title                    = models.CharField(max_length=255)
    stc_name                     = models.CharField(max_length=128)
    stc_pw                       = models.CharField(max_length=128)
    stc_contents                 = models.TextField()
    stc_author                   = models.CharField(max_length=128)
    stc_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    stc_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    stc_file01                   = models.FileField(upload_to='stc/file/%Y/%m/%d', null=True, blank=True)
    stc_file02                   = models.FileField(upload_to='stc/file/%Y/%m/%d', null=True, blank=True)
    stc_file03                   = models.FileField(upload_to='stc/file/%Y/%m/%d', null=True, blank=True)
    stc_file04                   = models.FileField(upload_to='stc/file/%Y/%m/%d', null=True, blank=True)
    stc_file05                   = models.FileField(upload_to='stc/file/%Y/%m/%d', null=True, blank=True)
    stc_img01                    = models.ImageField(upload_to='stc/img/%Y/%m/%d', null=True, blank=True)
    stc_img02                    = models.ImageField(upload_to='stc/img/%Y/%m/%d', null=True, blank=True)
    stc_img03                    = models.ImageField(upload_to='stc/img/%Y/%m/%d', null=True, blank=True)
    stc_img04                    = models.ImageField(upload_to='stc/img/%Y/%m/%d', null=True, blank=True)
    stc_img05                    = models.ImageField(upload_to='stc/img/%Y/%m/%d', null=True, blank=True)
    stc_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSptDev(models.Model):
    std_title                    = models.CharField(max_length=255)
    std_name                     = models.CharField(max_length=128)
    std_pw                       = models.CharField(max_length=128)
    std_contents                 = models.TextField()
    std_author                   = models.CharField(max_length=128)
    std_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    std_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    std_file01                   = models.FileField(upload_to='std/file/%Y/%m/%d', null=True, blank=True)
    std_file02                   = models.FileField(upload_to='std/file/%Y/%m/%d', null=True, blank=True)
    std_file03                   = models.FileField(upload_to='std/file/%Y/%m/%d', null=True, blank=True)
    std_file04                   = models.FileField(upload_to='std/file/%Y/%m/%d', null=True, blank=True)
    std_file05                   = models.FileField(upload_to='std/file/%Y/%m/%d', null=True, blank=True)
    std_img01                    = models.ImageField(upload_to='std/img/%Y/%m/%d', null=True, blank=True)
    std_img02                    = models.ImageField(upload_to='std/img/%Y/%m/%d', null=True, blank=True)
    std_img03                    = models.ImageField(upload_to='std/img/%Y/%m/%d', null=True, blank=True)
    std_img04                    = models.ImageField(upload_to='std/img/%Y/%m/%d', null=True, blank=True)
    std_img05                    = models.ImageField(upload_to='std/img/%Y/%m/%d', null=True, blank=True)
    std_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSclCommon(models.Model):
    scc_title                    = models.CharField(max_length=255)
    scc_name                     = models.CharField(max_length=128)
    scc_pw                       = models.CharField(max_length=128)
    scc_contents                 = models.TextField()
    scc_author                   = models.CharField(max_length=128)
    scc_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    scc_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    scc_file01                   = models.FileField(upload_to='scc/file/%Y/%m/%d', null=True, blank=True)
    scc_file02                   = models.FileField(upload_to='scc/file/%Y/%m/%d', null=True, blank=True)
    scc_file03                   = models.FileField(upload_to='scc/file/%Y/%m/%d', null=True, blank=True)
    scc_img01                    = models.ImageField(upload_to='scc/img/%Y/%m/%d', null=True, blank=True)
    scc_img02                    = models.ImageField(upload_to='scc/img/%Y/%m/%d', null=True, blank=True)
    scc_img03                    = models.ImageField(upload_to='scc/img/%Y/%m/%d', null=True, blank=True)
    scc_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSclFree(models.Model):
    scf_title                    = models.CharField(max_length=255)
    scf_name                     = models.CharField(max_length=128)
    scf_pw                       = models.CharField(max_length=128)
    scf_contents                 = models.TextField()
    scf_author                   = models.CharField(max_length=128)
    scf_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    scf_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    scf_file01                   = models.FileField(upload_to='scf/file/%Y/%m/%d', null=True, blank=True)
    scf_file02                   = models.FileField(upload_to='scf/file/%Y/%m/%d', null=True, blank=True)
    scf_file03                   = models.FileField(upload_to='scf/file/%Y/%m/%d', null=True, blank=True)
    scf_img01                    = models.ImageField(upload_to='scf/img/%Y/%m/%d', null=True, blank=True)
    scf_img02                    = models.ImageField(upload_to='scf/img/%Y/%m/%d', null=True, blank=True)
    scf_img03                    = models.ImageField(upload_to='scf/img/%Y/%m/%d', null=True, blank=True)
    scf_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSclRecommend(models.Model):
    scr_title                    = models.CharField(max_length=255)
    scr_name                     = models.CharField(max_length=128)
    scr_pw                       = models.CharField(max_length=128)
    scr_contents                 = models.TextField()
    scr_author                   = models.CharField(max_length=128)
    scr_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    scr_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    scr_file01                   = models.FileField(upload_to='scr/file/%Y/%m/%d', null=True, blank=True)
    scr_file02                   = models.FileField(upload_to='scr/file/%Y/%m/%d', null=True, blank=True)
    scr_file03                   = models.FileField(upload_to='scr/file/%Y/%m/%d', null=True, blank=True)
    scr_img01                    = models.ImageField(upload_to='scr/img/%Y/%m/%d', null=True, blank=True)
    scr_img02                    = models.ImageField(upload_to='scr/img/%Y/%m/%d', null=True, blank=True)
    scr_img03                    = models.ImageField(upload_to='scr/img/%Y/%m/%d', null=True, blank=True)
    scr_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaSclQanda(models.Model):
    scq_title                    = models.CharField(max_length=255)
    scq_name                     = models.CharField(max_length=128)
    scq_pw                       = models.CharField(max_length=128)
    scq_contents                 = models.TextField()
    scq_author                   = models.CharField(max_length=128)
    scq_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    scq_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    scq_file01                   = models.FileField(upload_to='scq/file/%Y/%m/%d', null=True, blank=True)
    scq_file02                   = models.FileField(upload_to='scq/file/%Y/%m/%d', null=True, blank=True)
    scq_file03                   = models.FileField(upload_to='scq/file/%Y/%m/%d', null=True, blank=True)
    scq_img01                    = models.ImageField(upload_to='scq/img/%Y/%m/%d', null=True, blank=True)
    scq_img02                    = models.ImageField(upload_to='scq/img/%Y/%m/%d', null=True, blank=True)
    scq_img03                    = models.ImageField(upload_to='scq/img/%Y/%m/%d', null=True, blank=True)
    scq_comments                 = models.PositiveSmallIntegerField(default=0, null=True)

class GayaEmpComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_emp                      = models.ForeignKey('GayaEmp')

class GayaCusComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_cus                      = models.ForeignKey('GayaCustomer')

class Gaya_HA201TP_Comments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_ha201tp                  = models.ForeignKey('HA201_TP')

class GayaMtrComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_mtr                      = models.ForeignKey('GayaMaterialInfo')

class GayaOrdComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_ord                      = models.ForeignKey('GayaOrder')

class GayaStlComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_stl                      = models.ForeignKey('GayaSptLinux')

class GayaStwComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_stw                      = models.ForeignKey('GayaSptWindows')

class GayaStvComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_stv                      = models.ForeignKey('GayaSptServer')

class GayaSttComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_stt                      = models.ForeignKey('GayaSptStorage')

class GayaStcComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_stc                      = models.ForeignKey('GayaSptSwitch')

class GayaStdComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_std                      = models.ForeignKey('GayaSptDev')

class GayaSccComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_scc                      = models.ForeignKey('GayaSclCommon')

class GayaScfComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_scf                      = models.ForeignKey('GayaSclFree')

class GayaScrComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_scr                      = models.ForeignKey('GayaSclRecommend')

class GayaScqComments(models.Model):
    com_name                     = models.CharField(max_length=64)
    com_pw                       = models.CharField(max_length=64)
    com_contents                 = models.TextField(max_length=2048)
    com_created                  = models.DateTimeField(auto_now_add=True, auto_now=False)
    com_modified                 = models.DateTimeField(auto_now_add=False, auto_now=True)
    com_scq                      = models.ForeignKey('GayaSclQanda')

