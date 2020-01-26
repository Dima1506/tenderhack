from django.http import HttpResponse
from django.shortcuts import render, redirect
import requests
import re
from django.conf import settings
from django.conf.urls.static import static
import json
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
import xmltodict, json
from datetime import timedelta, datetime, date, time
import requests
import dataset
import hashlib
import random
#db = dataset.connect('mysql://root:cxzaq15061999@localhost/iiko')




def index(request):
    try:
        print(request.session['uid'])
    except:
        t = hashlib.sha224(str(random.randint(10000, 1000000)).encode('UTF-8')).hexdigest()[0:14]
        print(t)
        request.session['uid'] = t
    return render(request, 'index.html', {'uid':request.session['uid']})

def news(request):
    return render(request, 'index_news.html', {'uid':request.session['uid']} )

def instr(request):
    return render(request, 'index_istr.html', {'uid':request.session['uid']})

def cont(request):
    return render(request, 'index_cont.html', {'uid':request.session['uid']})

def edu(request):
    return render(request, 'index_edu.html', {'uid':request.session['uid']})

@csrf_exempt
def post(request):
    print(request.GET)
    return HttpResponse('{"text":"dsads","button":[]}')
