from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import (
    home, register, CustomLoginView, submissions_list, problem_list, 
    problem_detail, profile_view
)

urlpatterns = [
    
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', views.problem_list, name='dashboard'),
    path('problems/', views.problem_list, name='problem_list'),
    path('problem/<int:problem_id>/', views.problem_detail, name='problem_detail'),
    path('submissions/', views.submissions_list, name='submissions_list'),
    path('profile/', views.profile_view, name='profile'),


    # API endpoints
    path('compile/', views.CodeCompileView.as_view(), name='code-compile'),
    path('submit/', views.CodeSubmissionView.as_view(), name='code-submit'),
]
