from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.skill_and_job_list, name='combined_list'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('save_job/<int:job_id>/', views.save_job, name='save_job'),
    path('request/<int:skill_id>/', views.request_session, name='request_session'),
    path('ajax/skill_filter/', views.ajax_skill_filter, name='ajax_skill_filter'),
    path('accounts/', include('django.contrib.auth.urls')),
]
