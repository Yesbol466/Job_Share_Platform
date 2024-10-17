from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Skill, Job, SavedJob

class UserRegistrationTest(TestCase):
    def test_user_registration(self):
        response = self.client.post(reverse('register'), {
            'username': 'newuser',
            'password1': 'complexpassword123',
            'password2': 'complexpassword123',
        })
        self.assertEqual(response.status_code, 302)  # Redirect to login
        self.assertTrue(User.objects.filter(username='newuser').exists())

class UserLoginTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_user_login(self):
        response = self.client.post(reverse('login'), {
            'username': 'testuser',
            'password': 'testpassword',
        })
        self.assertEqual(response.status_code, 302)  # Redirect after login
        self.assertTrue(response.wsgi_request.user.is_authenticated)

class SkillAndJobListTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        Job.objects.create(
            company='TestCompany',
            title='Software Engineer',
            category='Programming',
            location='USA',
            responsibility='Develop software',
            minimum_qualifications='BS in CS',
            preferred_qualifications='MS in CS'
        )

    def test_skill_and_job_list(self):
        response = self.client.get(reverse('combined_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Engineer') 
        self.assertContains(response, 'TestCompany') 
        self.assertContains(response, 'USA')  

class SaveJobTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.job = Job.objects.create(
            company='TestCompany',
            title='Software Engineer',
            category='Programming',
            location='USA',
            responsibility='Develop software',
            minimum_qualifications='BS in CS',
            preferred_qualifications='MS in CS'
        )

    def test_save_job(self):
        response = self.client.get(reverse('save_job', args=[self.job.id]))
        self.assertEqual(response.status_code, 302)  # Redirect after saving job
        self.assertTrue(SavedJob.objects.filter(user=self.user, job=self.job).exists())

class ProfilePageTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.job = Job.objects.create(
            company='TestCompany',
            title='Software Engineer',
            category='Programming',
            location='USA',
            responsibility='Develop software',
            minimum_qualifications='BS in CS',
            preferred_qualifications='MS in CS'
        )
        SavedJob.objects.create(user=self.user, job=self.job)

    def test_profile_page(self):
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Software Engineer') 
        self.assertContains(response, 'Profile updated successfully!', count=0) 
