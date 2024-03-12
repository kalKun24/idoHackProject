from django.urls import path
from . import views

urlpatterns = [
    path('exercise/', views.ExerciseListView.as_view(), name='exercise_list'),   
]
