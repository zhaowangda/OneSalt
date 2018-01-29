#coding=utf-8
from django import forms

class maintainCommand(forms.Form):
      minions = forms.CharField()
      module = forms.CharField()
      scripts = forms.CharField()


class LoginForm(forms.Form):
	"""docstring for ClassName"""
	username = forms.CharField(label="账号",max_length=20)
	password = forms.CharField(label="密码",widget=forms.PasswordInput())

