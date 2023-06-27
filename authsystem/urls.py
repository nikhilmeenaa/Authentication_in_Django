from django.urls import path
from .views import home_page , login_page , register_page, logout_user

urlpatterns = [
    path('', home_page.as_view(), name = "home_page"),    
    path('login', login_page.as_view(), name = "login_page"),    
    path('register', register_page.as_view(), name = "register_page"),    
    path('logout', logout_user, name = "logout_page"),    
]