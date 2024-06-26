from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm,CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import Record
from django.contrib import messages


# Create your views here.

#  Home Page

def home(request):
    
    # return HttpResponse("Hello World")
    return render(request, 'webapp/index.html')

#  Register Page

def register(request):
    """
    Register a new user.

    Parameters:
    request (HttpRequest): The HTTP request object.

    Returns:
    None. Renders the 'register.html' template with the provided form.

    If the request method is POST, it validates the form data, saves the new user to the database, and redirects to the login page.

    Raises:
    ValueError: If the form data is not valid.
    """
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Account Created Successfully!")
            return redirect("my-login")  

    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)

# Login a User

def my_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                messages.success(request,"You have Logged")
                return redirect("dashboard")
            

    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)

# Use Logout

def user_logout(request):
    auth.logout(request)
    messages.success(request,"Logout Success")
    return redirect("my-login")


# DashBoard View

@login_required(login_url="my-login")
def dashboard(request):

    my_records = Record.objects.all()
    context = {'records': my_records}

    return render(request, 'webapp/dashboard.html', context=context)



# Create a Record

@login_required(login_url="my-login")
def create_record(request):

    form = CreateRecordForm()
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Record was Created!")
            return redirect("dashboard")
        
    context = {'form': form}
    return render(request, 'webapp/create-record.html', context=context)


#Update a Record

@login_required(login_url="my-login")
def update_record(request, pk):

    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request,"Your Record was Updated!")
            return redirect("dashboard")
            
    context = {'form': form}
    return render(request, 'webapp/update-record.html', context=context)



# Read / View a Singular record
@login_required(login_url="my-login")
def singular_record(request, pk):
    all_records = Record.objects.get(id=pk)
    
    context = {'record': all_records}
    return render(request, 'webapp/view-record.html', context=context)

# Delete Record

@login_required(login_url="my-login")
def delete_record(request, pk):
    
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request,"Your Record was Deleted!")
    return redirect("dashboard")
