from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate,logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper

from . models import CompanyModel, AddEmployee
from . form import AddEmployeeForm,ContactForm
from . register import NewUserForm
# from .forms import NewUserForm

# Create your views here.


def company_home(request):
    diction = {"title": "welcome ",
            "employees": AddEmployee.objects.count()
               }
    return render(request, "company/company_home.html", context=diction)
###################################################

def add_employee(request, ):
    
    if request.method == "POST":
        form = AddEmployeeForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect("company:employee_report")
        else:
            
            return render(request, "company/add_employee.html",{"form": form})
        
    diction = {
        "title": "Add Employee",
        "form": AddEmployeeForm()
    }
    return render(request, "company/add_employee.html", context= diction)

#####################################################
# Employee Report
def employee_report(request):
    if "employee" not in request.session:
        request.session["employee"] = []
    return render(request, "company/employee_report.html",{"title": "Employee Report", "employees": AddEmployee.objects.all() })


####################################################
# company Rigster request 
def company_register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.error(request, "Registration Successful. ")

            return redirect("company:company_home")
        messages.error(request, "Unsuccessful registration. indalid information. ")
        
    diction = {"title": "Register ",
               "Company_register": NewUserForm(),
               }    
    return render(request, "company/company_register.html", context=diction)
######################################################
# company login request
def company_login(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username= username,password= password)
            if user is not None:
                login(request,user)
                messages.info(request,f"you are now logged in as {username}")
                return redirect("company:company_home")
            else:
                messages.info(request,"Invalid username or password")

    diction = {"title": "Login",
               "companyform": AuthenticationForm()}
    
    return render(request, "company/company_login.html", context=diction)
######################################################
# logout request 
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("index")
###################################################
# change password _____________________
def change_password(request):

    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect("company:company_login")
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    diction = {
        "title": "Change password",
        "change_password_form": form,
    }
    return render(request, "company/change_password.html", context=diction)
########################################## Contact page view
def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    diction = {
        "title": "Contact",
        "contact_form": ContactForm()
    }
    return render(request, "contact.html", context=diction)