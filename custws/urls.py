

from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('',home,name='home'),
    path('customer/home',userHome,name='user-home'),
    path('profile/',profileView,name='profile'),
    path('customer/dashboard',custDashBoard,name='dashboard'),
    path('customer/register',registerPage,name='register'),
    path('customer/login',LoginView.as_view(template_name='custws/login.html'),name='login'),
    path('customer/logout',LogoutView.as_view(template_name='custws/logout.html'),name='logout'),
    path('create/ticket',createTicketView,name='create-ticket'),
    path('make/payment/<int:id>',makePayment,name='payment'),

    path('customer/task/details/<uuid:pk>',TicketDetailView.as_view(template_name='custws/ticket_detail.html'),name='ticket-detail'),

]
