from django.urls import path
from .views import LandingPage
from . import views

app_name = 'lms'

urlpatterns = [
    path('', views.LandingPage, name = "LandingPage"),
    #path('SignUp/', SignUp.as_view(success_url = '/'), name = "Sign_up")
    #path('SignUp/', views.SignUp, name = "SignUp")
]
