from django import forms
from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from .models import CustomUser
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.contrib.auth import login as auth_login












class CustomSignupForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['full_name', 'company_name', 'employee_count', 'phone',]  # etc.







def request_reset(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        if user is not None:
            otp = reset_code()
            otp_created_at = timezone.now()

            otp_created_at_str = otp_created_at.isoformat()

            request.session["reset_otp"] = otp
            request.session["email"] = user.email
            request.session["otp_created_at"] = otp_created_at_str
            request.session["user_email"] = email
            send_mail('Forgot Password OTP',
                    f'Your OTP to reset your password is {otp}. Please use this code to complete the process.',
                    DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False
                    )
            cache.set(f'reset_otp_{email}', otp, timeout=300)
            return redirect('Verify')
            
    return render(request, 'request.html')

def verify_password(request):
    # email = request.data.get('email')
    if request.method == 'POST':
        otp = request.POST.get('otp')
        stored_otp = request.session['reset_otp']
        if otp == stored_otp:
            print(stored_otp)
            return redirect("Reset")
    return render(request, 'verify.html')
        
def reset_pass(request):
    if request.method == "POST":
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:
            email = request.session['email']
            user = get_object_or_404(User, email=email)
            user.set_password(password1)
            user.save()
    return render(request, 'reset.html')








def employee_root_redirect(request):
    return redirect('login')  # uses the "land" named URL


def all_employees(request):
    # your view code ...
   return render(request, 'all_employees.html')




def add_employee(request):
    return render(request, 'add employee.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# def signup(request):
#     return render(request, 'signup.html')

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

def all_employee(request):
    employee = Employee.objects.all()
    return render(request, 'all employee.html', {'employee': employee})

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


def signup(request):
    if request.method == 'POST':
        # Get form data
        full_name = request.POST.get('full_name', '').strip()
        email = request.POST.get('email', '').strip()
        company_name = request.POST.get('company_name', '').strip()
        phone = request.POST.get('phone', '').strip()
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        employee_count_str = request.POST.get('employee_count', '').strip()

        # Validate passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'signup.html')

        # Validate required fields
        if not all([full_name, email, password, company_name, employee_count_str]):
            messages.error(request, 'Please fill in all required fields.')
            return render(request, 'signup.html')

        # Convert employee count
        employee_count_mapping = {
            '1-10': 10,
            '11-50': 50, 
            '51-200': 200,
            '201-500': 500,
            '500+': 1000
        }
        employee_count = employee_count_mapping.get(employee_count_str, 0)

        try:
            # Check if user already exists by full name
            if CustomUser.objects.filter(full_name=full_name).exists():
                messages.error(request, 'A user with that full name already exists.')
                return render(request, 'signup.html')

            if CustomUser.objects.filter(email=email).exists():
                messages.error(request, 'A user with that email already exists.')
                return render(request, 'signup.html')

            # Create the user
            user = CustomUser.objects.create_user(
                email=email,
                password=password,
                full_name=full_name,
                company_name=company_name,
                phone=phone,
                employee_count=employee_count
            )

            messages.success(request, 'Account created successfully! You are now logged in.')
            auth_login(request, user)  # ✅ use auth_login to avoid name collision
            return redirect('land.html')  # Change to your actual dashboard URL name

        except Exception as e:
            messages.error(request, f'An error occurred while creating your account: {str(e)}')
            print(f"Signup error: {e}")  # For debugging

    return render(request, 'signup.html')




def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            return redirect('land')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    return render(request, 'login.html')








# def login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(request, username=email, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('employment/land.html')  # Redirect to a home page after signin
#         else:
#             return render(request, 'employment/login.html', {'error': 'Invalid credentials'})
#     return render(request, 'login.html')



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=20, required=False)  # Changed from phone_number to phone
    employee_count = forms.CharField(max_length=20, required=True)
    company_name = forms.CharField(max_length=255, required=True)  # Match model max_length
    full_name = forms.CharField(max_length=255, required=True)     # Match model max_length

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email', 'phone', 'company_name', 'employee_count', 'password1', 'password2')  # Changed phone_number to phone

    def save(self, commit=True):
        user = super().save(commit=False)
          # Use full_name as username
        user.email = self.cleaned_data['email']
        user.phone = self.cleaned_data['phone']  # Changed from phone_number to phone
        user.company_name = self.cleaned_data['company_name']
        user.full_name = self.cleaned_data['full_name']  # Add this line
        
        # Convert employee count string to number
        employee_count_mapping = {
            '1-10': 10,
            '11-50': 50, 
            '51-200': 200,
            '201-500': 500,
            '500+': 1000
        }
        user.employee_count = employee_count_mapping.get(self.cleaned_data['employee_count'], 0)
        
        if commit:
            user.save()
        return user