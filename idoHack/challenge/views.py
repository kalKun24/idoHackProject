from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CategoryModel, ExerciseModel, ChallengeModel

class ExerciseListView(ListView):
    model = ExerciseModel
    template_name = 'challenge/exercise_list.html'
    context_object_name = 'exercises'