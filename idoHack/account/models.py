from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    
    total_score = models.IntegerField(default=0, verbose_name="総得点") # ユーザの総得点
    biography = models.TextField(max_length=500, blank=True, verbose_name="自己紹介") # ユーザの自己紹介

    twitter_url = models.URLField(max_length=200, blank=True, verbose_name="TwitterURL") # ユーザのTwitterのURL
    github_url = models.URLField(max_length=200, blank=True, verbose_name="GitHubURL") # ユーザのGitHubのURL
    linkedin_url = models.URLField(max_length=200, blank=True, verbose_name="LinkedInURL") # ユーザのLinkedInのURL

    country = models.CharField(max_length=100, blank=True, verbose_name="国籍") # ユーザの国籍

    # ユーザの職業
    occupation = models.CharField(max_length=50, verbose_name="職業", choices=(('Student', '学生'),
                                          ('teacher', '教員'),
                                          ('SecurityEngineer', 'セキュリティエンジニア'),
                                          ('IT', 'IT職'),
                                          ('other', 'その他'))) 

    is_active = models.BooleanField(default=True, verbose_name="アクティブユーザ") # ユーザがアクティブかどうか
    is_staff = models.BooleanField(default=False, verbose_name="スタッフユーザ") # ユーザがスタッフかどうか
    is_writer = models.BooleanField(default=False, verbose_name="作問ユーザ") # ユーザが作問者かどうか    
