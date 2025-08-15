from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  login_view

urlpatterns = [
    
    path('signup/', views.signup, name='signup'),
    path('', views.land, name='employee_home'),

    path('add/', views.add_employee, name='add_employee'),
    path('all/', views.all_employee, name='all_employee'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('generate/', views.generateemployee, name='generate_employee'),
    path('contact/', views.contact, name='contact'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path('passwordcomplete/', views.passwordcomplete, name='password_complete'),
]