from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect ('reviews:index')
        else:
            messages.warning(request,"다시 입력하세요")
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request,'accounts/signup.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request,form.get_user())
            return redirect(request.GET.get('next') or 'accounts:index')
        else:
            messages.warning(request,'다시')
    else:
        form = AuthenticationForm()
    context={
        'form': form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')

def profile(request,username):
    User = get_user_model()
    profile_user = User.objects.get(username=username)
    context = {
        'profile_user': profile_user
    }
    return render(request,'accounts/profile.html',context)

def follow(request,username):
    User = get_user_model()
    #me 가 로그인한 사람 you 는 팔로잉 할 대상
    me = request.user
    you = User.objects.get(username=username)
    if me==you:
        return redirect('accounts:profile',you.username)
    if me in you.followers.all():
        you.followers.remove(me)
        print('취소')
    else:
        you.followers.add(me)
        print('성공')
    return redirect('accounts:profile',you.username)


def index(request):

    return render(request,'accounts/index.html')