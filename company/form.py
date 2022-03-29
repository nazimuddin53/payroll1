from django import  forms 

from . models import AddEmployee, CompanyModel,ContactUs

class AddEmployeeForm(forms.ModelForm):
    name = forms.CharField(label='Name')
    class Meta:
        model = AddEmployee
        fields = "__all__"
    
    # def save(self, comment=True):
    #     if request.method == "POST":
    #         form = super(AddEmployeeForm, self).save
    #         if commit:
    #             form.save()
    #         return form 
    
class CompanyForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = CompanyModel
        fields = ("username", "email", "password")
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"