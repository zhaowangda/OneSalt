"""onesalt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from saltModule import views




urlpatterns = [
    url(r'^admin', admin.site.urls),
    url(r'^index', views.index),
    url(r'^formboard', views.formboard),
    url(r'^grouplist', views.grouplist),
    url(r'^maintainonline', views.maintainonline),
    url(r'^login', views.login),
#    url(r'^', views.index),
    url(r'datacenterlist', views.datacenterList),
    url(r'datacenterinfo', views.datacenterInfo),
    url(r'deldatacenter', views.delDatacenter),
    url(r'modifydatacenter', views.modifyDatacenter),
    url(r'adddatacenterform', views.addDatacenterForm),
    url(r'adddatacenter', views.addDatacenter),

    url(r'machineroomlist', views.machineroomList),
    url(r'machineroomdelete', views.machineroomDelete),
    url(r'machineroomdetail', views.machineroomDetail),
    url(r'machineroomform', views.machineroomForm),
    url(r'machineroomadd', views.machineroomAdd),
    url(r'machineroommodify', views.machineroomModify),


    url(r'racklist', views.rackList),
    url(r'^rackaddform/$', views.rackAddForm),
    url(r'^rackaddrecord/$', views.rackAdd),
    url(r'rackdetail', views.rackDetail),
    url(r'rackdelete', views.rackDelete),
    url(r'rackmodify', views.rackModify),
    #-----------------------------------------
    #ajax
    url(r'getmachineroomsfromdatacenterid', views.getMachineRoomsFromDatacenterID),

    #test url ajax
    url(r'testajax', views.testAjax),

]

