from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'register'

urlpatterns = [
    path('SignUp/', views.SignUp, name = 'SignUp'),
    path('login/', auth_views.LoginView.as_view(template_name = 'Accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'Accounts/login.html'), name = 'logout')
]
