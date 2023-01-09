import datetime
from datetime import datetime
from datetime import date
from urllib import request
from .forms import SignUpForm, LoginForm
from pickle import TRUE
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from .models import History, Scheduler
from .forms import SchedulerForm
import os
from django.core.paginator import Paginator
from .models import ProgFile
import pandas as pd
from datetime import date
from django.db.models import Sum
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from APP.PROG.bkrcc import * 
from APP.PROG.bicasa import *
from APP.PROG.chargeback import *
from APP.PROG.chargeback1 import *
from APP.PROG.chargeback2 import *
from APP.PROG.chargeback3 import *
from APP.PROG.chargeback4 import *
from APP.PROG.pgi import *
from APP.PROG.reminder1 import *
from APP.PROG.reminder2 import *
from APP.PROG.tax_invoice import *
from APP.PROG.islm import *

def index(request):
    return render(request,'1index.html')

def logout(request):
    auth.logout(request)
    return redirect('/')


def user(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('showusers')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
        return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superadmin:
                login(request, user)
                print("--------------------------")
                print("welcome",username)
                return redirect('superadminhomepage')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('superadminhomepage')
            elif user is not None and user.is_user:
                login(request, user)
                return redirect('employee')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, '2login.html', {'form': form, 'msg': msg})

from django.contrib.auth import get_user_model
User = get_user_model()

@login_required
def superadminhomepage(request):

    now = datetime.now()
    start = now.strftime("%H:%M:%S")
    print("Current Time =", start)

    # ------------dashboardCount--------------------
    no_of_pdfs=History.objects.aggregate(Sum('Page')).values()
    total_clients=Scheduler.objects.values('CLIENT_NAME').distinct().count()

    total_daily_count=Scheduler.objects.filter(FREQUENCY='Daily').count()
    total_monthly_count=Scheduler.objects.filter(FREQUENCY='Monthly').count()
    total_yearly_count=Scheduler.objects.filter(FREQUENCY='Yearly').count()
    total_cycle_count=Scheduler.objects.filter(FREQUENCY='CYCLE').count()
    context={'no_of_pdfs':no_of_pdfs,'total_clients':total_clients,'total_daily_count':total_daily_count,'total_monthly_count':total_monthly_count,'total_yearly_count':total_yearly_count,'total_cycle_count':total_cycle_count}
    return render(request,'4superadmin_homepage.html',context)
def userhomepage(request):
    return render(request,'6user_homepage.html')
def adminhomepage(request):
    return render(request,'5admin_homepage.html')


def admin(request):
    return render(request,'admin.html')

def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'employee.html')

@login_required
def Newprocess(request):
    fm=SchedulerForm()
    if request.method=='POST':
        fm=SchedulerForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SchedulerForm()
    return render(request,'7new_process.html',{'form':fm}) 


@login_required
def schedulerdataadmin(request):
    if 'q' in request.GET:
        q=request.GET['q']
        datas=Scheduler.objects.filter(FILE_NAME__icontains=q)
    else:
        data=Scheduler.objects.all()
        p=Paginator(data,5)
        page=request.GET.get('page')
        datas=p.get_page(page)
    return render(request,'7schedular_data1.html',{'datas':datas})


@login_required
def schedulerdata(request):
    if 'q' in request.GET:
        q=request.GET['q']
        datas=Scheduler.objects.filter(FILE_NAME__icontains=q)
    else:
        data=Scheduler.objects.all()
        p=Paginator(data,5)
        page=request.GET.get('page')
        datas=p.get_page(page)
    return render(request,'7schedular_data.html',{'datas':datas}) 

@login_required
def showHistory(request):
    print('------------------------------------')
    if 'q' in request.GET:
        q=request.GET['q']
        datas=History.objects.filter(Product__icontains=q)
        return render(request,'8history_data.html',{'datas':datas}) 
    elif 'd1' in request.GET and 'd2' in request.GET:
        d1=request.GET['d1']
        d2=request.GET['d2']
        datas = History.objects.filter(Date__gte=d1)  
        return render(request,'8history_data.html',{'datas':datas})
    else:
        print('pagination')
        data=History.objects.all()
        p=Paginator(data,10)
        page=request.GET.get('page')
        datas=p.get_page(page)
    return render(request,'8history_data.html',{'datas':datas}) 


@login_required
def show(request):  
    user = User.objects.all()  
    return render(request,"6Show_user.html",{'user':user })  


@login_required
def schedulerdata(request):
    if 'q' in request.GET:
        q=request.GET['q']
        datas=Scheduler.objects.filter(FILE_NAME__icontains=q)
    else:
        data=Scheduler.objects.all()
        p=Paginator(data,5)
        page=request.GET.get('page')
        datas=p.get_page(page)
    return render(request,'7schedular_data.html',{'datas':datas}) 


@login_required
def startScheduler(request):
    print("--------------------------")
    print("Welcome In Project")
   #----------------------------Get FileNames from FOlder------------------------------
    mypath='E:\IWOC\SOURCE'
    from os import walk
    files1 = []

    for (dirpath, dirnames, filenames) in walk(mypath):
        files1.extend(filenames)
        break
    print('Files In Folder for execution',files1)

    f2=[]
    for i in files1:
        f2.append(os.path.splitext(i)[0][0:5])

    print("--------------------------")
    print('File names without ext ',f2)

    data1=Scheduler.objects.values_list('FILE_NAME', flat=True) #gives file names from database

    data1=list(data1)
    data1=[ x[0:5] for x in data1]
    df = pd.DataFrame(list(Scheduler.objects.all().values()))   
    df['FILE_NAME1']=df['FILE_NAME'].str.slice(0,5)
    for i in range(0,len(f2)):  
        if f2[i] in data1:
            df2=df.loc[df['FILE_NAME1'] == f2[i], 'PROGRAM_NAME']
            dest_loc =df.loc[df['FILE_NAME1'] == f2[i], 'OUT_FILE_DIRECTORY']
            if not df2.empty:
                for k in df2:
                    if not k.endswith('.exe'):
                        call_prog = df2.to_string(index = False)
                        call_p=call_prog
                        print("Program Executing ",call_prog)
                        print("File from Souce folder " +files1[i]," is Executing")
                        call_prog=eval(call_prog)
                        a=call_prog(request,files1[i])  

                        print("Program Execution Completed ",call_p)
                        print('------------------------------------------------')
                
    # return redirect(showHistory,files1)   
    exx = r'E:\i2s\MPC\PROGRAM'
    exe_files = []
    exe_file = os.listdir(r'E:\i2s\MPC\PROGRAM')
    for i in exe_file:
        if i.endswith('.exe'):
            exe_files.append(i)
    
    mypath ='E:\IWOC\SOURCE'
    from os import walk
    all_files = []

    for (dirpath, dirnames, filenames) in walk(mypath):
        all_files.extend(filenames)
        break
    print('Files In Folder for execution',all_files)

    f2=[]
    for i in all_files:
        f2.append(os.path.splitext(i)[0][0:])

    exe_src_files = []
    freq_for_exe_src = []
    exe_pgms = Scheduler.objects.values_list('PROGRAM_NAME',flat=True)
    schedular_exe_files = list(exe_pgms)
    for i in exe_files:
        for j in schedular_exe_files:
            if i == j:
                sche = Scheduler.objects.filter(PROGRAM_NAME=i)
                for k in sche:
                    exe_src_files.append(k.FILE_NAME)
                    freq_for_exe_src.append(k.FREQUENCY)
                
    finale_files_fm_src_to_run = []
    finale_files_fm_src_to_run1 = []
    for i in range(0,len(f2)):
        for j in exe_src_files:
            if f2[i] == j:
                finale_files_fm_src_to_run.append(f2[i])
                finale_files_fm_src_to_run1.append(f2[i] + '.txt')
    # print(finale_files_fm_src_to_run,'-0-------------------------------')
    file_name_from_scheduler = Scheduler.objects.values_list('FILE_NAME',flat=True).order_by('FILE_NAME')
    final_frequency = []
    for i in file_name_from_scheduler:
        for j in finale_files_fm_src_to_run:
            if i == j:
                sche = Scheduler.objects.filter(FILE_NAME=i)
                for k in sche:
                    final_frequency.append(k.FREQUENCY )
    print('Files From Source Folder Ready to Run',finale_files_fm_src_to_run)
    print('There Respective Frequency',final_frequency)
    EXE_FILE_MOVE_PATH = 'E:\i2s\MPC\OUTPUT\\'
    path21 = r'E:\IWOC\SOURCE'
    for k in range(0,len(finale_files_fm_src_to_run)):
        exe_file_path = EXE_FILE_MOVE_PATH + final_frequency[k]   + '\\'
        target1 = str(exe_file_path) 

        src_path = os.path.join(path21, finale_files_fm_src_to_run1[k])
        dst_path = os.path.join(target1, finale_files_fm_src_to_run1[k])
        os.rename(src_path, dst_path)
        print(finale_files_fm_src_to_run1[k],'File Moved to' , final_frequency[k])
    for i in exe_files:
        for j in schedular_exe_files:
            if i == j:
                exe_file_loc = exx + '\\'  + i
                os.system(exe_file_loc)
        

    return redirect(showHistory)
    
@login_required
def show(request):  
    user = User.objects.all()
    print(user,'-------------')  
    return render(request,"6Show_user.html",{'user':user })  


@login_required
def editusers(request, id):  
    user = User.objects.get(pk=id)  
    return render(request, '6Edit_user.html', {'user': user})  


@login_required
def updateusers(request,id):
    user=User.objects.get(pk=id)
    fm=SignUpForm(request.POST,instance=user)
    if fm.is_valid():
        fm.save()
        return redirect('/show')
    return render(request,'6Edit_user.html',{'user': user })


@login_required
def destroyusers(request, id):
    user = User.objects.get(id=id)  
    if request.method=='POST':  
        user.delete()  
        return redirect("/show")
    else:
        return render(request,"6Delete_user.html")


@login_required
def Newprocess(request):
    fm=SchedulerForm()
    if request.method=='POST':
        fm=SchedulerForm(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=SchedulerForm()
    return render(request,'7new_process.html',{'form':fm}) 

@login_required
def editprocess(request,id):
    pi = Scheduler.objects.get(pk=id)
    return render(request, '9editprocess.html',{'pi': pi })


@login_required
def updateprocess(request,id):
    pi=Scheduler.objects.get(pk=id)
    fm=SchedulerForm(request.POST,instance=pi)
    if fm.is_valid():
        fm.save()
        data=Scheduler.objects.all()
        p=Paginator(data,5)
        page=request.GET.get('page')
        datas=p.get_page(page)
        return render(request,'7schedular_data.html',{'datas':datas})
    return render(request,'templates/9editprocess.html',{'pi': pi })


@login_required
def deletep(request,id):
    dp = Scheduler.objects.get(pk=id)  
    if request.method=='POST':  
        dp.delete()  
        return redirect("/schedulerdata")
    else:
        return render(request,"9deleteprocess.html")


def SKRCC(request,files1):
    print(files1,'hELLO-------------------')
    return render(request,'8history_data.html')


def IWOC(request):
    print(request.BKRCC)
    print(request.BICASA)
    print(request.CHARGEBACK)
    print(request.CHARGEBACK1)
    print(request.CHARGEBACK2)
    print(request.CHARGEBACK3)
    print(request.CHARGEBACK4)
    print(request.PGI)
    print(request.REMINDER1)
    print(request.REMINDER2)
    print(request.TAX_INV)
    print(request.ISLM)


    


