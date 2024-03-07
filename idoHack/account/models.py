from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    total_score = models.IntegerField(default=0) # ユーザの総得点
    biography = models.TextField(max_length=500, blank=True) # ユーザの自己紹介

    twitter_url = models.URLField(max_length=200, blank=True) # ユーザのTwitterのURL
    github_url = models.URLField(max_length=200, blank=True) # ユーザのGitHubのURL
    linkedin_url = models.URLField(max_length=200, blank=True) # ユーザのLinkedInのURL

    country = models.CharField(max_length=100, blank=True) # ユーザの国籍

    # ユーザの職業
    occupation = models.CharField(max_length=50, choices=(('Student', '学生'),
                                          ('teacher', '教員'),
                                          ('SecurityEngineer', 'セキュリティエンジニア'),
                                          ('IT', 'IT職'),
                                          ('other', 'その他'))) 

    is_active = models.BooleanField(default=True) # ユーザがアクティブかどうか
    is_staff = models.BooleanField(default=False) # ユーザがスタッフかどうか
    is_writer = models.BooleanField(default=False) # ユーザが作問者かどうか    
