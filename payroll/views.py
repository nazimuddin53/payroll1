from django.shortcuts import render

def index(request):
    diction={"title":"Welcome Our Payroll System"}
    return render(request, 'index.html',context=diction)
# def logout_request(request):
#     logout(request)
# 	messages.info(request, "You have successfully logged out.") 
# 	return redirect("company:com")
