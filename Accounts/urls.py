
from django.urls import path
from . import views

urlpatterns = [
    path('',views.login_page,name='login_page'),
    path('register_page/',views.register_page,name = 'register-page'),
    path('home_page/',views.home_page,name = 'home'),
    path('logout_page/',views.logout_page,name='logout_page')
]
