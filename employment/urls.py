from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   
    path('land/', views.land, name='land'),
    path('add/', views.add_employee, name='add_employee'),
    path('all/', views.all_employee, name='all_employee'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('generate/', views.generateemployee, name='generate_employee'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('forgotpassword/', views.forgot_password, name='forgot_password'),
    path('passwordcomplete/', views.passwordcomplete, name='password_complete'),
    path('', auth_views.LoginView.as_view(template_name='land.html'), name='login'),

]


