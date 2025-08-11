from django.urls import path
from . import views

urlpatterns = [
    path('', views.land, name='employee_home'), 
    path('land/', views.land, name='land'),
    path('add/', views.add_employee, name='add_employee'),
    path('all/', views.all_employees, name='all_employees'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('generate/', views.generateemployee, name='generate_employee'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path('passwordcomplete/', views.passwordcomplete, name='password_complete'),
]

