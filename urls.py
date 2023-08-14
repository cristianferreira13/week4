from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('signup/', views.signup_view, name='signup'),


]
