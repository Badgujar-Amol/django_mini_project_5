from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from .models import Employee,Role,Department
from django.db.models import Q

def index(request):
    return render(request,'index.html')

def all_emp(request):
    details = Employee.objects.all()
    context = {
        'details': details
    }
    print(context)
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone = request.POST['phone']
        department = request.POST['department']
        role = request.POST['role']
        salary = request.POST['salary']
        bonus = request.POST['bonus']
        
        new_employee = Employee(first_name=first_name,last_name=last_name,phone=phone,dept_id=department,role_id=role,salary=salary,bonus=bonus,hire_date=datetime.now())
        new_employee.save()

        return HttpResponse ('Employee details added successfully')

    elif request.method =='GET':
        return render(request,'add_emp.html')
    else:
        return HttpResponse('An Exception Occured.! Employee has not been added ')

def remove_emp(request,emp_id = 0):

    if emp_id:
        try:
            emp_to_be_removed = Employee.objects.get(id = emp_id)
            emp_to_be_removed.delete()
            return HttpResponse('Employee Removed Successfully...!')
        except:
            return HttpResponse('Please Enter Valid Employee ID')

    details = Employee.objects.all()
    context = {
        'details': details
    }

    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']

        details = Employee.objects.all()

        if name:
            details = details.filter(Q(first_name__icontains = name) | (Q(last_name__icontains = name)))
        if dept:
            details = details.filter(dept__name__icontains = dept)
        if role:
            details = details.filter(role__name__icontains = role)

        context = {
            'details': details
        }
        return render(request,'all_emp.html',context)

    elif request.method =='GET':
        return render(request,'filter_emp.html')