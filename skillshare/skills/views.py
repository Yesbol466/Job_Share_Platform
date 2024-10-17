from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserProfileForm
from .models import Skill, Session, Job, SavedJob
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

@login_required
def skill_list(request):
    skills = Skill.objects.filter(availability=True)
    return render(request, 'skills/skill_list.html', {'skills': skills})

@login_required
def request_session(request, skill_id):
    skill = Skill.objects.get(id=skill_id)
    if request.method == 'POST':
        Session.objects.create(skill=skill, provider=skill.provider, requester=request.user, date=request.POST['date'], status='pending')
        return redirect('skill_list')
    return render(request, 'skills/request_session.html', {'skill': skill})

def ajax_skill_filter(request):
    query = request.GET.get('query', '')
    skills = Skill.objects.filter(name__icontains=query)
    data = [{'id': skill.id, 'name': skill.name, 'description': skill.description} for skill in skills]
    return JsonResponse({'skills': data})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'skills/register.html', {'form': form}) 

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'skills/job_list.html', {'jobs': jobs})

@login_required
def skill_and_job_list(request):
    category_filter = request.GET.get('category', None)
    skills = Skill.objects.all()
    jobs = Job.objects.all()

    if category_filter:
        skills = skills.filter(category=category_filter)
        jobs = jobs.filter(category=category_filter)

    return render(request, 'skills/combined_list.html', {
        'skills': skills,
        'jobs': jobs,
        'category_filter': category_filter,
    })

def home_view(request):
    if request.user.is_authenticated:
        return redirect('combined_list')
    else:
        form = AuthenticationForm()  # Login form
        return render(request, 'base.html', {'form': form})
    
@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)

    saved_jobs = SavedJob.objects.filter(user=request.user)
    
    return render(request, 'skills/profile.html', {'form': form, 'saved_jobs': saved_jobs})

@login_required
def save_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    SavedJob.objects.create(user=request.user, job=job)
    return redirect('combined_list')
