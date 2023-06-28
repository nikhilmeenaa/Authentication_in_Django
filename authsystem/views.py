from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.hashers import check_password
# Create your views here.


class home_page(View):
    def get(self,request):
        return render(request, "authsystem/home_page.html")
    def post(self,request):
        pass



class login_page(View):
    def get(self,request):
        return render(request, "authsystem/login_page.html")

    def post(self,request):
        uname = request.POST.get("username")
        passw = request.POST.get("pass")

        user = authenticate(request, username = uname , password = passw)
        # user = User.objects.get(username = uname)

        # print(uname)
        # print(passw)

        # if check_password(passw, user.password):
        if user is not None:
            login(request , user)
            return redirect("home_page")

        return HttpResponse("Username or password was incorrect!")



class register_page(View):
    def get(self, request):
        return render(request, "authsystem/register_page.html")

    def post(self,request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass")

        user = User(username = username , email = email)
        user.set_password(password)
        user.first_name = fname
        user.last_name = lname
        user.save()

        return HttpResponse(f"{fname} \n {lname} \n {email} \n {username} \n{password}")


def logout_user(request):
    logout(request)
    return redirect('login_page')


    