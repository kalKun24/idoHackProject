from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import CategoryModel, ExerciseModel, ChallengeModel

class ExerciseListView(ListView):
    model = ExerciseModel
    template_name = 'challenge/exercise_list.html'
    context_object_name = 'exercise_list'


#ToDo: Exercise内のChallengeを表示するViewを作成
class ExerciseDetailView(DetailView):
    model = ExerciseModel
    template_name = 'challenge/exercise_detail.html'
    context_object_name = 'exercise_detail'

    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['challenge_list'] = ChallengeModel.objects.filter(exercise_title=self.object)
        context['exercise_id'] = self.kwargs['pk']
        return context
    
#ToDo: Challengeの内容を表示するViewを作成
class ChallengeDetailView(DetailView):
    model = ChallengeModel
    template_name = 'challenge/challenge_detail.html'
    context_object_name = 'challenge_detail'

    # id=pksのChallengeを取得
    def get_object(self, queryset=None) -> Any:
        return ChallengeModel.objects.get(pk=self.kwargs['pks'])

    # id=pkのExercise内のChallengeを取得
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['challenge_list'] = ChallengeModel.objects.filter(exercise_title=self.kwargs['pk'])
        context['exercise_id'] = self.kwargs['pk']
        return context
