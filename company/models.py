from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class CompanyModel(models.Model):
    name = models.CharField(max_length = 222)
    username = models.CharField(max_length= 220)
    email = models.EmailField()
    password = models.CharField(max_length = 222)
    

    def __str__(self):
        return (f"Id : {self.id} UserName : {self.username} Name: {self.__name__} Email: {self.email} Password: {self.password}")


class AddEmployee(models.Model):
    name = models.CharField(max_length=122, help_text=u"Name")
    address = models.CharField(max_length=322)
    city = models.CharField(max_length=123)
    postalcode = models.IntegerField( )
    modile = models.IntegerField()
    signation = models.CharField(max_length= 44)
    branch = models.CharField(max_length=44)
    rank = models.CharField(max_length=10)
    basic_pay = models.IntegerField()
    bank_account = models.CharField(max_length=44)
    email = models.EmailField( max_length= 254)
    
    def __str__(self):
        return ( f"Name : { self.name } Signation :  {self.signation} Branch : {self.branch}  rank   {self.rank}")
class ContactUs(models.Model):

    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    mobile = models.IntegerField()
    email = models.EmailField()
    urls = models.URLField()
    message = models.TextField(max_length=1200)
    def __str__(self):
        return (f"Name : {self.first_name} Email : {self.email}")