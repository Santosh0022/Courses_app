from django.http import HttpResponse
from django.http import request
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.
def Register(request):
    if request.method == 'POST' :

        first_name = request.POST["firstname"]
        last_name  = request.POST["lastname"]
        username   = request.POST["Username"]
        password1  = request.POST["password"]
        password2  = request.POST["re-password"]
        email  = request.POST["Email"]
        user = User.objects.create_user(username = username, password =  password1, email =email, first_name = first_name, last_name = last_name)
        user.save()
        print("User Created")
        return redirect('/')
    else:
        return render( request,"Register.html")