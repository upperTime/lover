from django.shortcuts import render,redirect
from .froms import  LoginForm
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

def index(request):
    return render(request,'index.html')

@csrf_exempt
def loginlover(request):
    if request.method == "GET":
        return render(request, "login.html")
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('possword')
        message = '请检查填写的内容！'
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd["username"], password=cd["password"])
            if user:
                login(request, user)
                return redirect('/index')  # 重定向
            else:
                message = "登录失败，去问他吧"
                return render(request, "login.html", {"message": message})
    return redirect('/login')