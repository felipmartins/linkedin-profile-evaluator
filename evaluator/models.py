from email.policy import default
import uuid
from django.db import models

class Evaluation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url_name = models.CharField(max_length=255)
    profile_image = models.ImageField()
    background_image = models.ImageField()
    full_name = models.CharField(max_length=255)
    evaluation_date = models.DateField(auto_now_add=True)
    connections = models.IntegerField(default=0)
    about = models.TextField()
    head_title = models.CharField(max_length=255)
    education = models.JSONField()
    contact_info = models.JSONField()
    skills = models.JSONField()
    num_skills = models.IntegerField(default=0)
    recommendations = models.JSONField()
    num_recommendations = models.IntegerField(default=0)
    experience = models.JSONField()
    certifications = models.JSONField()
    languages = models.JSONField()
    projects = models.JSONField()
    num_projects = models.IntegerField(default=0)
    authoral_posts = models.IntegerField(default=0)
    has_changed_profile_image = models.BooleanField(default=False)
    face_found_in_profile_image = models.BooleanField(default=False)
    has_changed_background_image = models.BooleanField(default=False)
    has_email_in_contact_info = models.BooleanField(default=False)
    has_github_in_contact_info = models.BooleanField(default=False)
    has_key_words_in_title = models.BooleanField(default=False)
    has_about_section = models.BooleanField(default=False)
    has_trybe_in_education = models.BooleanField(default=False)
    has_3_or_more_authoral_posts = models.BooleanField(default=False)
    has_3_or_more_skills = models.BooleanField(default=False)
    has_3_or_more_projects = models.BooleanField(default=False)
    has_3_or_more_recommendations = models.BooleanField(default=False)
    has_200_or_more_connections = models.BooleanField(default=False)
    grade = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.full_name}: {self.grade}/100"