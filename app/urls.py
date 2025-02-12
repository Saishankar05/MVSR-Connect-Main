from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('teams/',views.teams,name='teams'),
    path('team/',views.team,name='team'),
    path('api/jobs/', views.JobAPIView.as_view(), name='jobs-api'),
    path('jobs/', views.JobListView.as_view(), name='job-list'),
    path('eve/',views.eve,name='eve'),
    
]