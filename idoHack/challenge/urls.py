from django.urls import path
from . import views

urlpatterns = [
    path('exercise/', views.ExerciseListView.as_view(), name='exercise_list'),   
    path('exercise/<int:pk>/tasks', views.ExerciseDetailView.as_view(), name='exercise_detail'),
    path('exercise/<int:pk>/tasks/<int:pks>/', views.ChallengeDetailView.as_view(), name='challenge_detail'),
]
