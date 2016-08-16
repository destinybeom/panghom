"""gy01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from gy01 import views

urlpatterns = [
    url(r'^$'                                 , views.Gaya_Home         , name='gaya_home'     ),
    url(r'^login/$'                           , 'django.contrib.auth.views.login'              ),
    url(r'^logout/$'                          , views.Gaya_Logout                              ),
    url(r'^password_change/$'                 , 'django.contrib.auth.views.password_change',
        {'post_change_redirect' : '/password_change/done/'}),
    url(r'^password_change/done/$'            , 'django.contrib.auth.views.password_change_done'),
    url(r'^pwon_add/$'                        , views.Emp_PWON           , name='emp_pwon'     ),
    url(r'^erp/'                              , include('erp.urls', namespace='erp')           ),
    url(r'^admin/'                            , include(admin.site.urls)                       ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
