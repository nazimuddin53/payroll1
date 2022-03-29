from django.urls import path 

from . import views

app_name = "company"
urlpatterns = [
    path("", views.company_home, name="company_home"),
    path("register/", views.company_register, name="company_register"),
    path("login/", views.company_login, name="company_login"),
    path("logout/", views.logout_request, name= "logout"),
    path("changepassword/", views.change_password, name="change_password"),
    path("add_employee/", views.add_employee, name="add_employee"),
    path("employee_report/", views.employee_report, name="employee_report"),
    path("contact/", views.contact, name="contact")
    
    
]   