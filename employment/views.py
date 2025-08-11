from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import redirect
# Views

def employee_root_redirect(request):
    return redirect('land')  # uses the "land" named URL


def add_employee(request):
    return HttpResponse("Add Employee.html")

def dashboard(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def land(request):
    return render(request, 'land.html')

def generateemployee(request):
    return render(request, 'generate employee.html')

def passwordcomplete(request):
    return render(request, 'password complete.html')

def forgot_password(request):
    return render(request, 'forgot password.html')

def form(request):
    return render(request, 'form.html')

def all_employees(request):
    employees = Employee.objects.all()
    return render(request, 'all_employees.html', {'employees': employees})

# Form class
class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    department = forms.CharField(max_length=50)

def employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            department = form.cleaned_data['department']
            return render(request, 'success.html', {'name': name})
    else:
        form = EmployeeForm()
    return render(request, 'employee_form.html', {'form': form})


