#coding:utf-8
from django.shortcuts import render


def home(request):
	string  = u'传递字符串'
	tlist = ['a','b','c','d','e']
	tdist = {1:'a',2:'b'}
	return render(request,'home.html',{'s':string,'tlist':tlist,'tdist':tdist})

def add(request,a,b):
	a = int(a)
	b = int(b)
	return HttpResponse(str(a+b))
