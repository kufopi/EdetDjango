from  django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('enter/', views.loginPage, name='login'),
    path('exit/', views.logoutPage, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('staff/', views.staffId, name='staffId'),
    path('deny/', views.denied, name='denied'),
    path('pg/', views.pgId, name='pgId'),


    

]
