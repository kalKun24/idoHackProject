from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CategoryModel, ExerciseModel, ChallengeModel

class ExerciseListView(ListView):
    model = ExerciseModel
    template_name = 'challenge/exercise_list.html'
    context_object_name = 'exercise_list'


class ExerciseDetailView(DetailView):
    model = ExerciseModel
    template_name = 'challenge/exercise_detail.html'
    context_object_name = 'exercise_detail'

class ChallengeListView(ListView):
    model = ChallengeModel
    template_name = 'challenge/challenge_list.html'
    context_object_name = 'challenge_list'

    # id=pkのExercise内のChallengeを取得
    def get_queryset(self) -> Any:
        return ChallengeModel.objects.filter(exercise_title=self.kwargs['pk'])

    # id=pkのExerciseを取得
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['exercise_detail'] = ExerciseModel.objects.get(pk=self.kwargs['pk'])
        return context
    
class ChallengeDetailView(DetailView):
    model = ChallengeModel
    template_name = 'challenge/challenge_detail.html'
    context_object_name = 'challenge_detail'

    # id=pksのChallengeを取得
    def get_object(self, queryset=None) -> Any:
        return ChallengeModel.objects.get(pk=self.kwargs['pks'])

    # id=pkのExerciseを取得
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['exercise_detail'] = ExerciseModel.objects.get(pk=self.kwargs['pk'])
        return context