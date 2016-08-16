from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from erp import models

# Register your models here.

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = models.GayaEmp
        fields = ('emp_email', 'emp_name', 'emp_rank', 'emp_phone', 'emp_address', 'emp_job')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = models.GayaEmp
        fields = ('emp_email', 'password', 'emp_name', 'emp_rank', 'emp_phone', 'emp_address', 'emp_job', 'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('emp_email', 'emp_name', 'emp_rank', 'emp_phone', 'emp_address', 'emp_job','is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('emp_email', 'password')}),
        ('Personal info', {'fields': ('emp_name', 'emp_rank', 'emp_phone', 'emp_address', 'emp_job',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('emp_email', 'emp_name', 'emp_rank', 'emp_phone', 'emp_address', 'emp_job', 'password1', 'password2')}
        ),
    )
    search_fields = ('emp_email',)
    ordering = ('emp_email',)
    filter_horizontal = ()

admin.site.register(models.GayaEmp, UserAdmin)
admin.site.register(models.GayaCustomer)
admin.site.register(models.GayaProductInfo)
admin.site.register(models.GayaMaterialInfo)
admin.site.register(models.GayaMaterialSN)
admin.site.register(models.GayaOrder)
admin.site.register(models.HA201_TP)
admin.site.register(models.AssembleReport)
admin.site.register(models.InspectionReport)
admin.site.register(models.PackagingReport)
admin.site.register(models.OrderReport)
admin.site.register(models.DeliveryReport)
admin.site.register(models.GayaSptLinux)
admin.site.register(models.GayaSptWindows)
admin.site.register(models.GayaSptServer)
admin.site.register(models.GayaSptStorage)
admin.site.register(models.GayaSptSwitch)
admin.site.register(models.GayaSptDev)
admin.site.register(models.GayaSclCommon)
admin.site.register(models.GayaSclFree)
admin.site.register(models.GayaSclRecommend)
admin.site.register(models.GayaSclQanda)

admin.site.unregister(Group)
