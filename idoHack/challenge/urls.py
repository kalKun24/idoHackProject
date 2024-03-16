from django.urls import path
from . import views

urlpatterns = [
    path('exercise/', views.ExerciseListView.as_view(), name='exercise_list'),   
    path('exercise/<int:pk>/detail/', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/<int:pk>/tasks/', views.ChallengeListView.as_view(), name='challenge_list'),
    path('exercise/<int:pk>/tasks/<int:pks>/', views.ChallengeDetailView.as_view(), name='challenge_detail'),
    path('exercise/<int:pk>/textbook/', views.TextbookView.as_view(), name='textbook'),
    path('exercise/<int:pk>/explanation/', views.ExplanationView.as_view(), name='explanation'),
    path('exercise/<int:pk>/submit/', views.SubmitView.as_view(), name='submit'),
]
