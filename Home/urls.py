from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('verify', views.verify, name='verify'),
    
    path('target-plan', views.target_plan, name='target_plan'),
    
    path('chat', views.portfolio_advice, name='lyzr_chat'),  # New endpoint for Lyzr AI integration
    path('retrive-chat', views.retrive_chat, name='retrive_chat'),  # New endpoint for Lyzr AI integration

]
