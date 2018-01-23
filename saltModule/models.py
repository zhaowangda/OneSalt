# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class  user(models.Model):
    name = models.CharField(max_length=20,null=False)
    email = models.EmailField()
    passwd = models.CharField(max_length=20,null=False)
    enabled = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name
#--------------------------------------------------------------
#salt stack job tables

class  jids(models.Model):
	jid = models.CharField(max_length=255,null=False,unique=True)
	load = models.TextField(null=False)


class  salt_returns(models.Model):
	#id  = models.CharField(max_length=255,null=False),
	fun = models.CharField(max_length=50,null=False)
	jid = models.CharField(max_length=255,null=False)
	Return = models.TextField(null=False)
	success = models.CharField(max_length=10,null=False)
	full_ret = models.TextField(null=False)
	alter_time = models.DateField(auto_now_add=True)
 

class  salt_events(models.Model):
    #id BIGINT NOT NULL AUTO_INCREMENT
	tag = models.CharField(max_length=255,null=False)
	data = models.TextField(null=False)
	alter_time = models.DateField(auto_now_add=True)
	master_id = models.CharField(max_length=255,null=False)

#--------------------------------------------------------------
#datacenter mgmt  tables	
class  datacenters(models.Model):
    #id BIGINT NOT NULL AUTO_INCREMENT
	name = models.CharField(max_length=255,null=False)
	address = models.CharField(max_length=255,null=False)
	power1 = models.CharField(max_length=255,null=False) # 电路1
	power2 = models.CharField(max_length=255,null=True) # 电路2
	TEMPMin = models.IntegerField(default=18,null=False) #温度：单位摄氏度
	TEMPMax = models.IntegerField(default=22,null=False) #温度：单位摄氏度
	HRMin = models.IntegerField(default=30,null=False)   #相对湿度最小值%relative humidity
	HRMax = models.IntegerField(default=70,null=False)   #相对湿度最小值%relative humidity 
	supplier = models.CharField(max_length=255,null=True) #提供商
	MRNumber = models.IntegerField(default=0,null=True) #机房数量
	rackNumber = models.IntegerField(default=0,null=True) #机架数量
	state = models.IntegerField(default=0,null=False)    #使用状态
	remark = models.TextField(null=True)    #备注信息


class  machinerooms(models.Model):
    #id BIGINT NOT NULL AUTO_INCREMENT
	sn = models.CharField(default="",max_length=255,null=False)
	name = models.CharField(max_length=255,null=False)
	datacenterid = models.ForeignKey(datacenters, on_delete=models.CASCADE)
	userDefineName = models.CharField(max_length=255,null=True)
	power1 = models.CharField(max_length=50,null=True) # 电路1
	power2 = models.CharField(max_length=50,null=True) # 电路2
	TEMPMin = models.IntegerField(default=18,null=False) #温度：单位摄氏度
	TEMPMax = models.IntegerField(default=22,null=False) #温度：单位摄氏度
	HRMin = models.IntegerField(default=30,null=False)   #相对湿度最小值%relative humidity
	HRMax = models.IntegerField(default=70,null=False)   #相对湿度最小值%relative humidity 
	capacityUnit = models.IntegerField(default=0,null=True) #总U位
	rackNumber = models.IntegerField(default=0,null=True) #机架数量
	state = models.IntegerField(default=0,null=False)    #使用状态
	remark = models.TextField(null=True)    #备注信息

class  racks(models.Model):
    #id BIGINT NOT NULL AUTO_INCREMENT
	sn = models.CharField(default="",max_length=255,null=False)
	name = models.CharField(max_length=255,null=False)
	machineRoomID = models.ForeignKey(machinerooms, on_delete=models.CASCADE)
	userDefineName = models.CharField(max_length=255,null=True)
	power1 = models.CharField(default="2.2kW",max_length=50,null=True) # 电路1
	power2 = models.CharField(default="2.2kW",max_length=50,null=True) # 电路2
	TEMPMin = models.IntegerField(default=18,null=False) #温度：单位摄氏度
	TEMPMax = models.IntegerField(default=22,null=False) #温度：单位摄氏度
	HRMin = models.IntegerField(default=30,null=False)   #相对湿度最小值%relative humidity
	HRMax = models.IntegerField(default=70,null=False)   #相对湿度最小值%relative humidity 
	capacityUnit = models.IntegerField(default=0,null=True) #总U位
	rackNumber = models.IntegerField(default=0,null=True) #  下一版本需要删除
	state = models.IntegerField(default=0,null=False)    #使用状态
	remark = models.TextField(null=True)    #备注信息


