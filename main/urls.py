from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage, name='index'),
    # managers urls
    path('staff/manager/login', ManagerLogin, name='manager_login'),
    path('staff/manager/logout', ManagerLogout, name='manager_logout'),
    path('staff/manager/dashboard', ManagerDashboard, name='manager_dashboard'),
    path('staff/manager/dashboard/my_profile', ManagerDashboard_profile, name='manager_profile'),
    path('staff/manager/dashboard/our_team', ManagerDashboard_team, name='manager_team'),
    path('staff/manager/dashboard/stacks', ManagerDashboard_stacks, name='manager_stacks'),
    path('staff/manager/dashboard/stacks/<int:pk>/details', ManagerDashboard_stacksEdit, name='manager_stacksEdit'),
    
]