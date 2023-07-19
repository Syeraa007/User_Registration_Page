from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from APp.models import *
from APp.forms import *

def registration(request):
    d={'UFO':UserForm(),'PFO':ProfileForm()}
    if request.method=='POST' and request.FILES:
        UFD=UserForm(request.POST)
        PFD=ProfileForm(request.POST,request.FILES)
        if UFD.is_valid() and PFD.is_valid():
            NSUFO=UFD.save(commit=False)
            pushpswd=UFD.cleaned_data['password']
            NSUFO.set_password(pushpswd)
            NSUFO.save()
            NSPFO=PFD.save(commit=False)
            NSPFO.username=NSUFO
            NSPFO.save()
            return HttpResponse('Registration Successfully done')
        else:
            return HttpResponse('Invalid Data Entered')
    return render(request,'registration.html',d)

def topicPageRecord(request):
    d={'TFO':TopicForm(),'PFO':PageForm(),'RFO':RecordForm()}
    if request.method=='POST':
        TFD=TopicForm(request.POST)
        PFD=PageForm(request.POST)
        RFD=RecordForm(request.POST)
        if TFD.is_valid() and PFD.is_valid() and RFD.is_valid():
            NSTFO=TFD.save(commit=False)
            # TI=TFD.cleaned_data['topic']
            NSTFO.save()
            NSPFO=PFD.save(commit=False)
            # NSPFO.topic=TI
            NSPFO.topic=NSTFO
            NSPFO.save()
            NSRFO=RFD.save(commit=False)
            NSRFO.name=NSPFO
            NSRFO.save()
            return HttpResponse('All Details Taken Successfully')
        else:
            return HttpResponse('Invalid Details')
    return render(request,'topicPageRecord.html',d)