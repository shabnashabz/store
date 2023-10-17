from pickle import NONE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth import login

from django.contrib.auth.hashers import make_password, check_password

from storeapp.models import Registration
def home(request):
   return render(request, 'index.html')
def signup(request):
  if request.method == 'POST':
      username = request.POST['username']
     
      pass1 = request.POST['pass1']
      pass2 = request.POST['pass2']
      if pass1==pass2:
         if User.objects.filter(username=username).exists():
             messages.info(request,"Username taken")
             return redirect('signup')
        
         else:
          myuser = User.objects.create_user(username,pass1)
     
          myuser.save()
    
         messages.info(request,"Successfully created")
         return redirect('signin')
      else:
        messages.info(request,"password is incorrect")
        return redirect('signup')
    
  return render(request, 'signup.html')
def signin(request):
    if request.method == 'POST':
      username = request.POST['username']
      pass1= request.POST['pass1']
      user = authenticate(username=username, password=pass1)
      if user is not None:
         login(request, user)
        
         return render(request, 'index.html', {'user': user})
      else:
         messages.error(request,"Invalid username or password")
         return redirect('signin')
    
    else:
        return render(request, 'signin.html')
    
def index(request):
    return render (request,'index.html')
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user=authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return redirect('/')
        else:  
            messages.error(request,"invalid credential")
            return redirect('register')  
    
    return render(request,"login.html")

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
         if User.objects.filter(username=username).exists():
             messages.info(request,"Username taken")
             return redirect('register')
       
         else:
          user=User.objects.create_user(username=username, password=password,)
          user.save()
          messages.success(request,"Successfully Registered")
          return redirect('login')
         print("user created")
        else:
            messages.info(request,"password is incorrect")
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')
def custom_404_view(request, exception):
    # Return a custom error page
    return render(request, 'custom_404.html', status=404)
def new_page(request):
    if request.method == 'POST':
        p=Registration()
        p.user_id = request.POST.get('user_id')
        p.name = request.POST.get('name')
        p.dob = request.POST.get('dob')
        p.age = request.POST.get('age')
        p.gender = request.POST.get('gender')
        p.phn = request.POST.get('phone')
        p.email = request.POST.get('email')
        p.add = request.POST.get('address')
        p.depart = request.POST.get('department')
        p.course = request.POST.get('course')
        p.purpose = request.POST.get('purpose')
        p.material= ', '.join(request.POST.getlist('materials'))
        p.save()
        return HttpResponse("Hello, this is the new page!")
    return render(request, 'new_page.html')
    
    
    
    
# # def login(request): 
# #     if request.method == 'POST': 
# #         username = request.POST.get('username') 
#         password = request.POST.get('password')
#         try: 
#             user = User.objects.get(username=username)
#             if check_password(password, user.password):
#                 messages.success(request, 'Logged in successfully.')
#                 return redirect('home') # Redirect to a success page.
#             else:
#                 messages.error(request, 'Username and password do not match')
#         except User.DoesNotExist: 
#             messages.error(request,'User does not exist')  
#     return render(request, 'login.html')  # Login failed page.
# def register_user(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('cpassword')

#         # Check if the username is already taken
#         if User.objects.filter(username=username).exists():
#             return HttpResponse('Username already taken.')

#         # Check if the passwords match
#         if password != cpassword:
#             return HttpResponse('Passwords do not match.')

#         # Create a new User object and save it to the database
#         user = User(username=username, password=password)
#         user.save()

#         return HttpResponse('Registration successful!')
#     else:
#         return render(request, 'register.html')