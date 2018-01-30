# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader,Context

from django.shortcuts import render_to_response

import forms
from  saltFun import runningCommandOnline

import django.middleware.csrf

from django.template import RequestContext

from django.shortcuts import redirect
import models
import json
from django.core import serializers
from django.forms.models import model_to_dict

# Create your views here.


def login(request):
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        if login_form.is_valid():
            login_name = request.POST['username'].strip()
            login_password = request.POST['password'].strip()
            try:
                user = models.user.objects.get(name=login_name)
                if user.passwd == login_password:
                    response = redirect('/')
                    request.session['username'] = user.name
                    request.session['usermail'] = user.email
                    return redirect('/maintainonline')
                else:
                    message = "账号或密码错误"
            except Exception, e:
                    message =  e
        else:
            message = "输入内容的格式不对"
    else:
        login_form = forms.LoginForm()

    template = loader.get_template('login.html')

    #request_context = RequestContext(request)

    c = Context({"vars":locals()})
    #request_context.push(locals())
    html = template.render(locals())
    response = HttpResponse(html)
    return response








def index(request):
    t = loader.get_template('mainPageTemplate.html')
    c = Context({"name":"test"})
    c = {}
    return HttpResponse(t.render(c))


##----------------------------------------------------
#datacenter module
def datacenterList(request):
    t = loader.get_template('datacenterlist.html')
    c = Context({"name":"test"})
    allDatacenter = models.datacenters.objects.all()
    c = {"allDatacenter":allDatacenter}
    return HttpResponse(t.render(c))

def datacenterInfo(request):
    t = loader.get_template('datacenterInfo.html')
    dtID = request.GET['datacenterID']
    datacenter = models.datacenters.objects.get(id=dtID)
    c = {"datacenter":datacenter}
    return HttpResponse(t.render(c))



def delDatacenter(request):
    dtID = request.GET['datacenterID']
    models.datacenters.objects.filter(id=dtID).delete()
    return redirect("/datacenterlist")

def modifyDatacenter(request):
    dtID = request.POST['id']
    datacenter = models.datacenters.objects.get(id=dtID)
    datacenter.name = request.POST['name'].strip()
    datacenter.state = request.POST['state']
    datacenter.supplier = request.POST['supplier'].strip()
    datacenter.MRNumber = request.POST['MRNumber']
    datacenter.rackNumber = request.POST['rackNumber']
    datacenter.power1 = request.POST['power1']
    datacenter.power2 = request.POST['power2']
    datacenter.TEMPMin = request.POST['TEMPMin']
    datacenter.TEMPMax = request.POST['TEMPMax']
    datacenter.HRMin = request.POST['HRMin']
    datacenter.HRMax = request.POST['HRMax']
    datacenter.remark = request.POST['remark'].strip()
    datacenter.save()
    return redirect("/datacenterlist")

def addDatacenterForm(request):
    t = loader.get_template('addDatacenterForm.html')
    c = {}
    return HttpResponse(t.render(c))

def addDatacenter(request):
    #dtID = request.POST['id']
    datacenter = models.datacenters()
    datacenter.name = request.POST['name'].strip()
    datacenter.state = request.POST['state']
    datacenter.supplier = request.POST['supplier'].strip()
    datacenter.MRNumber = request.POST['MRNumber']
    datacenter.rackNumber = request.POST['rackNumber']
    datacenter.power1 = request.POST['power1']
    datacenter.power2 = request.POST['power2']
    datacenter.TEMPMin = request.POST['TEMPMin']
    datacenter.TEMPMax = request.POST['TEMPMax']
    datacenter.HRMin = request.POST['HRMin']
    datacenter.HRMax = request.POST['HRMax']
    datacenter.remark = request.POST['remark'].strip()
    datacenter.save()
    return redirect("/datacenterlist")

#-------
#machineRoom module

def machineroomList(request):
    t = loader.get_template('machineroomlist.html')
    c = Context({"name":"test"})
    allMachineRoom = models.machinerooms.objects.all()
    c = {"allMachineRoom":allMachineRoom}
    return HttpResponse(t.render(c))



def machineroomDetail(request):
    t = loader.get_template('machineroomdetail.html')
    ID = request.GET['machineroomid']
    machineroom = models.machinerooms.objects.get(id=ID)
    c = {"machineroom":machineroom}
    return HttpResponse(t.render(c))


def machineroomDelete(request):
    dtID = request.GET['machineroomid']
    models.machinerooms.objects.filter(id=dtID).delete()
    return redirect("/machineroomlist")

def machineroomModify(request):
    ID = request.GET['machineroomid']
    machineroom = models.machinerooms.objects.get(id=ID)
    machineroom.name = request.POST['name'].strip()
    machineroom.userDefineName = request.POST['userDefineName'].strip()
    machineroom.state = request.POST['state']
    machineroom.capacityUnit = request.POST['capacityUnit']
    machineroom.rackNumber = request.POST['rackNumber']
    machineroom.power1 = request.POST['power1']
    machineroom.power2 = request.POST['power2']
    machineroom.TEMPMin = request.POST['TEMPMin']
    machineroom.TEMPMax = request.POST['TEMPMax']
    machineroom.HRMin = request.POST['HRMin']
    machineroom.HRMax = request.POST['HRMax']
    machineroom.remark = request.POST['remark'].strip()
    machineroom.save()
    return redirect("/machineroomlist")

def machineroomForm(request):
    t = loader.get_template('machineroomFormAdd.html')
    c = Context({"name":"test"})
    allDatacenter = models.datacenters.objects.all()
    c = {"allDatacenter":allDatacenter}
    return HttpResponse(t.render(c))

def machineroomAdd(request):
    machineroom = models.machinerooms()
    machineroom.name = request.POST['name'].strip()
    machineroom.userDefineName = request.POST['userDefineName'].strip()
    machineroom.sn = request.POST['sn']
    machineroom.state = request.POST['state']
    machineroom.capacityUnit = request.POST['capacityUnit']
    machineroom.rackNumber = request.POST['rackNumber']

    machineroom.power1 = request.POST['power1']
    machineroom.power2 = request.POST['power2']
    machineroom.TEMPMin = request.POST['TEMPMin']
    machineroom.TEMPMax = request.POST['TEMPMax']
    machineroom.HRMin = request.POST['HRMin']
    machineroom.HRMax = request.POST['HRMax']
    machineroom.datacenterid = models.datacenters.objects.get(id=request.POST['datacenterid'])

    machineroom.remark = request.POST['remark'].strip()
    machineroom.save()
    return redirect("/machineroomlist")


#-------
#racks module

def rackList(request):
    t = loader.get_template('racklist.html')
    c = Context({"name":"test"})
    racks = models.racks.objects.all()
    c = {"racks":racks}
    return HttpResponse(t.render(c))


def rackDetail(request):
    t = loader.get_template('rackdetail.html')
    ID = request.GET['id']
    rack = models.racks.objects.get(id=ID)
    c = {"rack":rack}
    return HttpResponse(t.render(c))

def rackAddForm(request):

    t = loader.get_template('rackAddForm.html')
    allDatacenter = models.datacenters.objects.all()
    c = {"allDatacenter":allDatacenter}
    return HttpResponse(t.render(c))

def rackAdd(request):
    rack = models.racks()
    rack.sn = request.POST['sn'].strip()
    rack.name = request.POST['name'].strip()
    rack.userDefineName = request.POST['userDefineName'].strip()
    rack.state = request.POST['state']
    rack.capacityUnit = request.POST['capacityUnit']
    rack.machineRoomID = models.machinerooms.objects.get(id=request.POST['machineroom'])

    rack.power1 = request.POST['power1']
    rack.power2 = request.POST['power2']
    rack.TEMPMin = request.POST['TEMPMin']
    rack.TEMPMax = request.POST['TEMPMax']
    rack.HRMin = request.POST['HRMin']
    rack.HRMax = request.POST['HRMax']
    rack.remark = request.POST['remark'].strip()
    rack.save()
    return redirect("/racklist")

def rackModify(request):
    ID = request.GET['id']
    rack = models.racks.objects.get(id=ID)
    #rack.sn = request.POST['sn'].strip()
    #rack.name = request.POST['name'].strip()
    rack.userDefineName = request.POST['userDefineName'].strip()
    rack.state = request.POST['state']
    rack.capacityUnit = request.POST['capacityUnit']

    rack.power1 = request.POST['power1']
    rack.power2 = request.POST['power2']
    rack.TEMPMin = request.POST['TEMPMin']
    rack.TEMPMax = request.POST['TEMPMax']
    rack.HRMin = request.POST['HRMin']
    rack.HRMax = request.POST['HRMax']
    rack.remark = request.POST['remark'].strip()
    rack.save()
    return redirect("/racklist")

def rackDelete(request):
    ID = request.GET['id']
    models.racks.objects.filter(id=ID).delete()
    return redirect("/racklist")


#------------------------------
# ajax Get machineRooms from datacenter
def getMachineRoomsFromDatacenterID(request):
    datacenterID = request.GET['id']
    machineroomlist = models.machinerooms.objects.filter(datacenterid=datacenterID)
    
    data = {}
    for  machineroom in machineroomlist:
        data[machineroom.id] = machineroom.name +"-->"+machineroom.userDefineName
    #
    #print data
    #data = json.dumps(model_to_dict(machineroomlist))
    data = json.dumps(data)
    return HttpResponse(data, content_type='application/json')


def testAjax(request):
    t = loader.get_template('testAjax.html')
    allDatacenter = models.datacenters.objects.all()
    c = {"allDatacenter":allDatacenter}
    return HttpResponse(t.render(c))



#-----------------------------------------------------



def formboard(request):
    t = loader.get_template('formboard.html')
    c = Context({"name":"test"})
    c = {}
    return HttpResponse(t.render(c))


#-----------------------------------------------
# automation

def grouplist(request):
    t = loader.get_template('zdh-grouplist.html')
    c = Context({"name":"test"})
    c = {}
    return HttpResponse(t.render(c))

def maintainonline(request):
    jobid = ""
    if request.method=="POST":
          minions = request.POST['minions']
          module = request.POST['module']
          scripts = str(request.POST['scripts'])
          print minions + ";"+module +";"+scripts 
          result = runningCommandOnline( minions, module, scripts )
          #jobid = result
          t = loader.get_template('zdh-maintainOnLine.html')
          #c = Context({"result":result })
          
          #return HttpResponse(t.render(result))
          return HttpResponse(t.render(locals()))
    else:
          pass 
    t = loader.get_template('zdh-maintainOnLine.html')
    c = Context({"job":jobid})
    c = {}
    return HttpResponse(t.render(c))
 

