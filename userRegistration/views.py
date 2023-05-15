
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import CustomUser,MyForm
import datetime
from .form import userRegistrationForm,userLoginForm
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .form import MyUserForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.views.decorators.cache import cache_control
from django.contrib.auth import logout
from django.core.mail import send_mail
from django.conf import settings






@login_required(login_url='login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    return render(request,'registration/home.html')


@login_required(login_url='login')
def regisration(request):
    if request.method == 'POST':
        print('1')
        email = request.user.email
        print(email)
        form = MyUserForm(request.POST, request.FILES)
        if form.is_valid():
            print(11)
            form.save()
            messages.success(request, "data submitted !!!")
            # Send email
            subject = 'Member Registration Data Submission Succesful'
            message = 'Your Member registration form for Dhaka University IT Society has been submitted successfully!!!.'
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list)
            return redirect('/home')
        if not form.is_valid():
            print(form.errors)
    else:
        print('2 isnot valid')
        form = MyUserForm()
    print('3 is not valid ')
    context = {'form': form}
    return render(request, 'registration/registration.html', context)


def success(request):
    return render(request, 'registration/success.html')


@login_required(login_url='login')
def profile(request):
    registration_number = request.user.registration_no
    print(registration_number,'1')

    try:
        print('11')
        myform = MyForm.objects.get(registration_number=registration_number)
        context = {'myform': myform}
        return render(request, 'registration/profile.html', context)
    except MyForm.DoesNotExist:
        print('12')
        return render(request, 'registration/profile.html')


def signup(request):
 if request.method == 'POST':
    registration_no = request.POST.get('registration_no')
    email = request.POST.get('email')
    password = request.POST.get('password')
    confirm_password = request.POST.get('confirm_password')
    print(password, confirm_password)

    if password == confirm_password:
        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, 'email already exists')
            return redirect('/signup')
        elif CustomUser.objects.filter(registration_no=registration_no).exists():
            messages.error(request, 'you are already registered by your registration number')
            return redirect('/signup')
        else:
            user = CustomUser(
                registration_no=registration_no,
                email=email,
                password=make_password(password),
                date_joined=datetime.datetime.now(),
                last_login=datetime.datetime.now(),
                is_active=True,
                is_admin=False,
                is_superuser=False,
                is_staff=False,
            )
            user.save()

            # Authenticate and login user
            authenticated_user = authenticate(request, registration_no=registration_no, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                messages.success(request, 'User authenticated and logged in successfully')
            else:
                messages.error(request, 'Unable to authenticate user')

            return redirect('/')

    else:
        messages.error(request, 'password do not match')
        return redirect('/signup')

 else:
    return render(request, 'registration/signup.html')


def login_view(request):
    if request.method == 'POST':
        registration_no = request.POST.get('registration_no')
        print('r',registration_no)
        password = request.POST.get('password')
        print('s',password)
        user = authenticate( registration_no=registration_no, password=password)
        if user is not None:
            print('1')
            login(request, user)
            if request.user.is_authenticated:
               return redirect('/home')
        else:
            print('2')
            error_message = "Invalid login credentials"
    else:
        error_message = None
        print(error_message,'3')
    return render(request, 'registration/login.html', {'error_message': error_message})


# logout functionality 
def logout_view(request):
    logout(request)
    # Replace '/login' with your desired redirect URL after logout
    return redirect('/login')
