#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse

def add_actiton(request):
	return HttpResponse('<a href="/add">加法<a>')

def add(request):
	a = request.GET.get('a',0)
	b = request.GET.get('b',0)

	c = int(a) + int(b)
	return HttpResponse(str(c))

def add2(request,a,b):
	a = int(a)
	b = int(b)
	c = str(a+b)
	return HttpResponse(c)

