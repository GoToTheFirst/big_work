from django.shortcuts import render, HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.db.models import Max
import datetime
from .models import Employee
# Create your views here.


def is_logined(request):
    is_login_success = request.COOKIES.get("is_login_success")
    if is_login_success == None:
        is_login_success = False
    if is_login_success:
        print(is_login_success)
    else:
        print("cuo")
        return HttpResponse("zheshiceshi")



def add_emp(request):
    return render(request, "shi_tu/addEmp.html")


def add_emp_msg(request):
    name = request.POST.get("name")
    emps = Employee.objects.filter()
    for foo in emps:
        print(name)
        print(foo.name)
        if name == foo.name:
            return HttpResponse('该员工已存在!<a href="/employee/add_emp/">返回</a>' )

    salary = request.POST.get("salary")
    salary = int(salary)
    age = request.POST.get("age")
    age = int(age)
    gender = request.POST.get("gender")
    if gender=="m":
        gender = "男"
    else:
        gender = "女"
    birth = datetime.datetime.now().year - age
    birth = str(birth)

    birth = birth + "-" + request.POST.get("birth")

    empl = Employee.objects.all()
    # print(len(empl))
    empl = len(empl) + 1
    emp = Employee.objects.create(e_id=empl, name=name, salary=salary, age=age, birth=birth, gender=gender)
    emp.save()
    return HttpResponseRedirect("/employee/emplist/")
    # if name is not None & salary is not None & age is not None & birth is not None & gender is not None:
    #     print('不是空的')
    #     emp = Employee.objects.create(e_id=empl, name=name, salary=salary, age=age, birth=birth , gender=gender)
    #     emp.save()
    #     return HttpResponseRedirect("/employee/emplist/")
    # else:
    #     return HttpResponse("输入内容不能为空  <a href='/employee/add_emp/'>点击返回</a>")
    # return render(request, "/employee/emplist/")
    #return render(request, 'shi_tu/emplist.html', {'mana': Employee.objects.all()})
    # return HttpResponseRedirect("/employee/emplist/")


def emplist(request):
    # is_logined(request)
    if request.COOKIES.get("is_login_success"):
        man_all = Employee.objects.all()
        i =1
        for foo in man_all:
            foo.e_id = i
            foo.save()
            i = i+1
        return render(request, 'shi_tu/emplist.html', {'mana': Employee.objects.all()})
        #return render(request, 'shi_tu/emplist.html', {'mana':Manager.objects.all(),'i': 1})
    else:
        return HttpResponseRedirect("/login/")

#跳转到修改
def update_emp(request):
    e_id = int(request.GET.get("e_id"))-1
    emp = Employee.objects.filter()[e_id]
    print("修改员工名字："+emp.name)
    return render(request, 'shi_tu/updateEmp.html', {'emp': emp, 'e_id': e_id+1})


def update(request):
    e_id = int(request.GET.get('e_id')) - 1
    emp = Employee.objects.filter()[e_id]
    emp.name = request.POST.get('name')
    emp.salary = request.POST.get('salary')
    emp.age = int(request.POST.get('age'))
    gender = request.POST.get('gender')
    if gender=='m':
        gender = '男'
    else:
        gender = '女'

    emp.gender = gender
    # birth = datetime.datetime.now().year - int(request.POST.get('age'))
    # birth = str(birth)
    # birth = birth + "-" + request.GET.get("birth")
    # emp.birth = birth
    emp.birth = request.POST.get("birth")
    emp.save()
    return HttpResponseRedirect('/employee/emplist/')


def delete_emp(request):
    e_id = int(request.GET.get('e_id')) - 1
    print(e_id)
    emp = Employee.objects.filter()[e_id]
    emp.delete()
    return HttpResponseRedirect('/employee/emplist/')
