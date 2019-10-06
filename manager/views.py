from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from .models import Manager
from django.template import loader ,Context
from django.http import HttpResponse
import datetime


#获取注册内容，添加到数据库
def register(request):
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    real_name = request.POST.get("real_name")
    gender = request.POST.get("gender")
    manager = Manager.objects.create(user_name=user_name, password=password, real_name=real_name, gender=gender)
    manager.save()
    #request = HttpResponse('shi_tu/login.html')
    #return render(request, 'shi_tu/login.html')
    return HttpResponseRedirect("/login/")


#访问注册页面
def zhu_ce(request):
    time_now = [datetime.datetime.now().year, datetime.datetime.now().month, datetime.datetime.now().day]
    print(time_now)
    return render(request, 'shi_tu/regist.html', {'time': time_now})


def login(request):
    return render(request, 'shi_tu/login.html')


#验证登录
def login_confirm(request):
    user_name = request.POST.get("user_name")
    password = request.POST.get("password")
    manger = Manager.objects.filter(user_name = user_name)
    is_login_success = False
    if manger != None:
        for m in manger:
            if m.password == password:
                is_login_success = True
                break
        if is_login_success:
            # print (Manager.objects.all())
            # return render(request, 'shi_tu/emplist.html', {'mana':Manager.objects.all(),'i': 1})
            response = HttpResponse('登录成功！<a href="/employee/emplist/">点击跳转</a>')
            rember_password = request.POST.get("rember_password")
            print(rember_password)
            if rember_password == 'rem':
                response.set_cookie('user_name', user_name, 60*60*60*24*15)
                response.set_cookie('password', password, 60*60*60*24*15)
                print("存入cookie")
            response.set_cookie('is_login_success', is_login_success, 60 * 5)

            return response
            # return HttpResponse('登录成功！<a href="http://127.0.0.1:8000/employee/emplist/">点击跳转</a>')
        else:
            return HttpResponse("账号不存在或密码错误<a href='/login/'>点击返回登录</a>")
    else:
        return HttpResponse("账号不存在<a href='/login/'>点击返回登录</a>")


