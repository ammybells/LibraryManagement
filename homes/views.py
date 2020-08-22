
from django.shortcuts import render 



def LandingPage(request):
    return render(request, 'homes/index.html')



