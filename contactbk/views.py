from django.shortcuts import render
from django.http import HttpResponse
from .models import contact

def ct(request):
    return render(request,"contactbk.html")


def create (request):
    try:
        Name = request.POST['name']
        num =request.POST['mob']
        cr=contact(name=Name,phone_number=num)
        cr.save()
        return render (request,"contactbk.html",{"msg1":"Contact added"})
    except Exception as e:
        print(e)
        return render(request,"contactbk.html",{"msg1":"Contact can't be added"})
    

def display(request):
    ds=contact.objects.all()
    return render (request,"contactbk.html",{"dis":ds})

def delete(request):
    Name=request.POST['deltname']
    de=contact.objects.filter(name=Name)
    de.delete()
    return render(request,"contactbk.html",{"msg2":"Deleted"})

def updatenam(request):
    try:
        Oldname=request.POST['oldname']
        Newname=request.POST['newname']
        up=contact.objects.filter(name=Oldname)
        if up.exists():
            up.update(name=Newname)
            return render(request,"contactbk.html",{'msg3':" Name Updated "})
        else :
            return render (request,"contactbk.html",{'msg':"No records"})
    except Exception as e:
        print(e)
        return render(request,"contactbk.html",{'msg4':"Not Updated"})
    

def updatenum(request):
    try:
        oldnum=request.POST['name2']
        nuwnum=request.POST['newnumber']
        upn=contact.objects.filter(name=oldnum)
        if upn.exists():
            upn.update(phone_number=nuwnum)
            return render(request,"contactbk.html",{"msg5" : "Number Updated"})
        else :
            return render(request,"contactbk.html",{'msg':"No records"})
    except Exception as e:
        print(e)
        return render (request,"contactbk.html",{'msg6' : "Not Updated"})




                  