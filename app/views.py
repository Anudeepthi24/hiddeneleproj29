from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse

def create_school(request):
    ESFO=SchoolForm()
    d={'ESFO':ESFO}

    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            sn=SFDO.cleaned_data['Sname']   
            sp=SFDO.cleaned_data['Sprincipal']
            sloc=SFDO.cleaned_data['Slocation']
            e=SFDO.cleaned_data['email']
            r=SFDO.cleaned_data['re-enteremail']
            SO=School.objects.get_or_create(Sname=sn,Sprincipal=sp,Slocation=sloc,email=e,re_enteremail=r)[0]
            SO.save()
            return HttpResponse('School is created')
        else:
            return HttpResponse('invalid data')
    return render(request,'create_school.html',d)
    
       












