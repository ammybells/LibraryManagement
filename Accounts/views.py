from django.shortcuts import render, redirect
#from django.contrib.auth.models import User, auth
from .forms import SignUpForm
from django.contrib.auth import login, authenticate,logout

# Create your views here.
def SignUp(request):
    if request.method == 'POST':
        register = SignUpForm(request.POST)
        if register.is_valid():
            register.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username = username, password = password)
            login(request, user)
            return redirect('books:books_list')
        
  
        
    else:
        register = SignUpForm()   
    context = {'register': register}  
    return render(request, 'Accounts/SignUp.html', context)






'''
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email_address = request.POST['email_address']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect('SignUp/')

            elif User.objects.filter(email_address = email_address).exists():
                messages.info(request, 'Email Address already exists')
                return redirect('SignUp/')

            else:
                
                user = User.objects.create_user(username = username, password1 = password2, email_address = email_address, first_name = first_name , last_name = last_name)
                user.save()
            
                messages.info(request, 'Sign Up Sucessful')
                return redirect('books/')
                 
            
    

        else: 
            messages.info(request, 'Ensure the Passwords match')
            return redirect('/')
        '''