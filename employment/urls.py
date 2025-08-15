from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import  login_view

urlpatterns = [
    
    path('', views.signup, name='signup'),
    path('land/', views.land, name='land'),

    path('add/', views.add_employee, name='add_employee'),
    path('all/', views.all_employee, name='all_employee'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('generate/', views.generate_employee, name='generate_employee'),
    path('contact/', views.contact, name='contact'),

    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path('passwordcomplete/', views.password_complete, name='password_complete'),
]