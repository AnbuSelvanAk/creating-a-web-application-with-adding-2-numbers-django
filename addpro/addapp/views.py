from django.shortcuts import render
from django.http import HttpResonse
def testing(requst):
	a=30
	b=50
	c=a+b
	x=x='<h1>A VALUE IS....'+str(a)+'B VALUE IS...'+str(b)='SUM VALUE IS....'+str(c)+'</h1>'
	HttpResonse(x)