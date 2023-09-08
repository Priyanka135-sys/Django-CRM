
from django.urls import path
from . import views

urlpatterns = [
    
    path('',views.home,name='home'),
    #path('login/',views.login_users,name='login'),
    path('logout/',views.logout_users,name='logout'),
    path('regisgter/',views.register_users,name='register'),

]