from django import forms
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Employee, CustomUser

# ---------------------------
# Forms
# ---------------------------
class CustomSignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'company_name', 'employee_count', 'phone']


class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    department = forms.CharField(max_length=50)


# ---------------------------
# Views
# ---------------------------

@login_required(login_url='/login/')
def land(request):
    return render(request, 'land.html')


def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name', '')
        email = request.POST.get('email', '').lower()
        company_name = request.POST.get('company_name', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')

        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return render(request, 'signup.html')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already exists. Please log in.")
            return redirect('login')

        user = CustomUser.objects.create_user(
            email=email,
            password=password,
            full_name=full_name,
            company_name=company_name,
            phone=phone
        )

        login(request, user)
        return redirect('land')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email', '').lower()
        password = request.POST.get('password', '')
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('land')
        else:
            messages.error(request, "Invalid email or password.")
            return render(request, 'login.html')

    return render(request, 'login.html')


def all_employee(request):
    employees = Employee.objects.all()
    return render(request, 'all employee.html', {'employee': employees})


def add_employee(request):
    return render(request, 'add employee.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def generate_employee(request):
    return render(request, 'generate employee.html')


def password_complete(request):
    return render(request, 'password complete.html')


def forgot_password(request):
    return render(request, 'forgot password.html')


# ---------------------------
# Form view for /form/
# ---------------------------
def form(request):
    """This is the view linked to path('form/', views.form)"""
    return render(request, 'form.html')


def employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            return render(request, 'success.html', {'name': name})
    else:
        form = EmployeeForm()
    return render(request, 'employee form.html', {'form': form})
