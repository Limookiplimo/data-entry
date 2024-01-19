from django.shortcuts import render
from .forms import EmployeeForm

# Create your views here.
def enroll_employee(request):
    form = EmployeeForm()
    
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()

    context = {"form":form}
    return render(request, "enrolls/enroll.html", context)

def user_login():
    pass

def register_user():
    pass