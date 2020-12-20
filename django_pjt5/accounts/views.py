from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    User = get_user_model()
    users = User.objects.all()
    context={
        'users':users
    }
    return render(request,'accounts/index.html',context)

# Create your views here.
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            return redirect ('accounts:index')
        else:
            messages.warning(request,"다시 입력하세요")
    else:
        form = UserCreationForm()
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

