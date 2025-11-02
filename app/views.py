from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def display_dept(request):
    QLDO = Dept.objects.all()   
    d = {'QLDO': QLDO}
    return render(request, 'display_dept.html', d)

def display_emp(request):
    #QLEO = Emp.objects.filter(Q(ename='Smith')&Q(job='clerk')) 
    QLEO=Emp.objects.all()

    d = {'QLEO': QLEO}
    return render(request, 'display_emp.html', d)
   

def display_salgrade(request):
    QLSO = Salgrade.objects.all()   
    d = {'QLSO': QLSO}
    return render(request, 'display_salgrade.html', d)

   
