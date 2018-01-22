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

 		

