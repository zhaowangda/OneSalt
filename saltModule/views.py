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



def machineRoomList(request):
    t = loader.get_template('machineRoomList.html')
    c = Context({"name":"test"})
    allMachineRoom = models.machinerooms.objects.all()
    c = {"allMachineRoom":allMachineRoom}
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
 

