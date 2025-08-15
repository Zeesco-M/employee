from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect

def redirect_to_employee(request):
    return redirect('employee/')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', redirect_to_employee),
    path('employee/', include('employment.urls')),
    path('', lambda request: redirect('land')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]    


