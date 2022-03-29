from django.contrib import admin
from .models import CompanyModel, AddEmployee,ContactUs

# Register your models here.
admin.site.register(CompanyModel)
admin.site.register(AddEmployee)
admin.site.register(ContactUs)
