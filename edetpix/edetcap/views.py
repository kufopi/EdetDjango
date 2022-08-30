
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import UniversityStaff, Session,User,Postgrad
from django.contrib.auth.models import  Group
from .forms import UserRegisterForm, UserUpdateForm, UniversityStaffForm,PostgradForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from datetime import datetime, date, timedelta
# Create your views here.


def uni_group_check(user):
    if user:
        return user.groups.filter(name='University Staff').exists() 
    return False


def pg_group_check(user):
    if user:
        return user.groups.filter(name='Postgrad').exists() 
    return False



def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST) 
        if form.is_valid():
            user=form.save() 
            user.username = form.cleaned_data.get('username') 
            login(request,user)
            messages.success(request, f'Your account has been created! Just 1 more important form') 
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

@login_required(login_url='login')
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user)
        # p_form = ProfileUpdateForm(request.POST,
        #                            request.FILES,
        #                            instance=request.user.profile) 
        if u_form.is_valid():
            person = u_form.save(commit=False)
            us = User.objects.get(username=person.username)
            
            grpcat = person.category
            person.save()
            group = Group(name=grpcat)
            gp,created= Group.objects.get_or_create(name=group) 

            person.groups.add(gp)
            print(grpcat)
            # if group.DoesNotExist:
            #     print('True True does not exist')  
            #     #group.save()
            #     us.groups.add(group)
            # else:
            #     print(f'Group {group}--==user:{us}')
            #     us.groups.add(group)
            
            


            #p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('home') # Redirect back to profile page

    else:
        u_form = UserUpdateForm(instance=request.user)
        #p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form
        
    }

    return render(request, 'profile.html', context)

@login_required(login_url='login')
def home(request):
    return render(request,'home.html')


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        #email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user= authenticate(request,username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Username or Password is incorrect")

    context={
        'page':page
    }

    return render(request,'register.html', context)

def logoutPage(request):
    logout(request)
    return redirect('login')

@login_required
@user_passes_test(uni_group_check, login_url='denied')
def staffId(request):
    tit = 'Staff ID'
    form = UniversityStaffForm()
    comeback = date.today()+timedelta(days=20)
    comeback2 = comeback + timedelta(days=10)
    if request.method=="POST":
        desi = request.POST.get('designation')
        sessi = Session.objects.all()[0]
        UniversityStaff.objects.create(
            fellow = request.user,
            staff_id = request.user.staff_id,
            first_name=request.user.first_name ,
            middle_name= request.user.middle_name,
            surname = request.user.surname,
            gender= request.user.gender,
            designation = desi,
            session = sessi,
            blood_group= request.user.blood_group,
            
        )
        
        messages.success(request, f'Your request has been submitted!')
        
        messages.success(request, f'''Please return between {comeback.strftime("%d/%b/%Y")} and {comeback2.strftime("%d/%b/%Y")} to get your ID card''')
        return redirect('home')
    else:
        form=UniversityStaffForm()
    context ={
        'form':form,
        'tit':tit
    }
    return render(request,'uniform.html',context)

def denied(request):
    return render(request,'denied.html')


@login_required
@user_passes_test(pg_group_check, login_url='denied')
def pgId(request):
    tit = 'Postgraduate ID'
    form = PostgradForm()
    comeback = date.today()+timedelta(days=20)
    comeback2 = comeback + timedelta(days=10)
    if request.method=="POST":
        desi = request.POST.get('level')
        dept = request.POST.get('department')
        sessi = Session.objects.all()[0]

        if Postgrad.objects.filter(fellow=request.user,session = sessi).exists():
            messages.warning(request, f'''You have made a replacement request within the same session!,
            Visit Mr Edet (ICT Unit) with a Sworn Affidavit and \u20A6 2000 penalty fee''')



        Postgrad.objects.create(
            fellow = request.user,
            staff_id = request.user.staff_id,
            first_name=request.user.first_name ,
            middle_name= request.user.middle_name,
            surname = request.user.surname,
            gender= request.user.gender,
            level = desi,
            department=dept,
            session = sessi,
            blood_group= request.user.blood_group,

        )
        print(f'this is dessi {desi}')
        
        messages.success(request, f'''Your request has been submitted!''')
        messages.success(request, f'''Please return between {comeback.strftime("%d/%b/%Y")} and {comeback2.strftime("%d/%b/%Y")} to get your ID card''')
        return redirect('home')
    else:
        form=PostgradForm()
    context ={
        'form':form,
        'tit':tit
    }
    return render(request,'uniform.html',context)


        
    