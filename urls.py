# habits/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('habit/create/', views.habit_create_view, name='habit_create'),
    path('habit/<int:habit_id>/edit/', views.habit_edit_view, name='habit_edit'),
    path('habit/<int:habit_id>/delete/', views.habit_delete_view, name='habit_delete'),

    path('track_habit/', views.track_habit, name='track_habit'),
]
