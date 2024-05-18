from django.shortcuts import render,redirect
from .models import House
from .forms import HouseForm
# Create your views here.

def house_list(request):
    records=House.objects.all()
    mydict={'records':records}
    return render(request,'Listingpage.html',context=mydict)

def AddHouse(request):
    mydict={}
    form=HouseForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('/')

    mydict['form']=form
    return render(request,'Add.html',mydict)

def EditHouse(request,id=None):
    one_rec=House.objects.get(pk=id)
    form=HouseForm(request.POST or None,request.FILES or None, instance=one_rec)
    if form.is_valid():
        form.save()
        return redirect('/')
    mydict= {'form':form}
    return render(request,'Edit.html',context=mydict)

def DeleteHouse(request,eid=None):
    one_rec = House.objects.get(pk=eid)
    if  request.method=="POST":
         one_rec.delete()
         return redirect('/')
    return render(request,'Delete.html')

def ViewHouse(request,eid=None):
    mydict={}
    one_rec = House.objects.get(pk=eid)
    mydict['House']=one_rec
    return render(request,'''View.html''',mydict)

def Login(request):
    return render(request, 'Login.html')

def signin(request):
    return render(request, 'Signin.html')