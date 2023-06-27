from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User

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
        username = request.POST.get("username")
        password = request.POST.get("pass")
        return HttpResponse(f"{username} \n {password}")



class register_page(View):
    def get(self, request):
        return render(request, "authsystem/register_page.html")

    def post(self,request):
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("pass")
        return HttpResponse(f"{fname} \n {lname} \n {email} \n {username} \n{password}")

