from django.db import models
from django.contrib.auth.models import User

class Skill(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    provider = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='General')
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Session(models.Model):
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    provider = models.ForeignKey(Skill, related_name='provided_sessions', on_delete=models.CASCADE)
    requester = models.ForeignKey(Skill, related_name='requested_sessions', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('rejected', 'Rejected')])

    def __str__(self):
        return f"{self.skill.name} - {self.date}"


class Job(models.Model):
    company = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    responsibility = models.TextField()
    minimum_qualifications = models.TextField()
    preferred_qualifications = models.TextField()

    def __str__(self):
        return f"{self.title} at {self.company}"


class SavedJob(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} saved {self.job.title}"
