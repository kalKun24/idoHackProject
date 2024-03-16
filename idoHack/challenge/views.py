from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CategoryModel, ExerciseModel, ChallengeModel, SubmitModel
from account.models import CustomUser
from django.shortcuts import redirect
from django.contrib import messages

class ExerciseListView(LoginRequiredMixin, ListView):
    model = ExerciseModel
    template_name = 'challenge/exercise_list.html'
    context_object_name = 'exercise_list'


class ExerciseDetailView(LoginRequiredMixin, DetailView):
    model = ExerciseModel
    template_name = 'challenge/exercise_detail.html'
    context_object_name = 'exercise_detail'

class ChallengeListView(LoginRequiredMixin, ListView):
    model = ChallengeModel
    template_name = 'challenge/challenge_list.html'
    context_object_name = 'challenge_list'

    # id=pkのExercise内のChallengeを取得
    def get_queryset(self) -> Any:
        # ExerciseModelのtitle="実戦問題"なら、is_practice=TrueのChallengeModelをExercise関係なく取得
        if ExerciseModel.objects.get(pk=self.kwargs['pk']).exercise_title == "実戦問題集":
            return ChallengeModel.objects.filter(is_practice=True)
        else:
            return ChallengeModel.objects.filter(exercise_title=self.kwargs['pk'])

    # id=pkのExerciseを取得
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['exercise_detail'] = ExerciseModel.objects.get(pk=self.kwargs['pk'])
        return context
    
class ChallengeDetailView(LoginRequiredMixin, DetailView):
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
    
    # Flagのチェック
    def post(self, request, *args, **kwargs):
        challenge = ChallengeModel.objects.get(pk=self.kwargs['pks'])
        user = CustomUser.objects.get(username=request.user)
        flag = request.POST['submit_flag']

        # ユーザがすでに回答済みかどうか
        if challenge.flag != flag:
            messages.add_message(request, messages.ERROR, "不正解です。")
            
        elif SubmitModel.objects.filter(challenge_title=challenge, username=user).exists():
            messages.add_message(request, messages.INFO, "正解です！(ただし、すでに回答済みです)")

        elif challenge.flag == flag:
            submit = SubmitModel(challenge_title=challenge, username=user)
            submit.save()
            user.total_score += challenge.score
            user.save()
            messages.add_message(request, messages.SUCCESS, "正解です！おめでとうございます！")


        # 自分にリダイレクト
        return redirect('challenge_detail', pk=self.kwargs['pk'], pks=self.kwargs['pks'])


class TextbookView(LoginRequiredMixin, DetailView):
    model = ExerciseModel
    template_name = 'challenge/textbook.html'
    context_object_name = 'exercise_detail'

class ExplanationView(LoginRequiredMixin, DetailView):
    model = ExerciseModel
    template_name = 'challenge/explanation.html'
    context_object_name = 'exercise_detail'


# Exerciseごとの提出状況
class SubmitView(LoginRequiredMixin, ListView):
    model = SubmitModel
    template_name = 'challenge/exercise_submit.html'
    context_object_name = 'submit_list'

    # id=pkのExercise_titleを持つChallenge_titleのSubmitを取得
    def get_queryset(self) -> Any:
        exercise = ExerciseModel.objects.get(pk=self.kwargs['pk'])
        challenge = ChallengeModel.objects.filter(exercise_title=exercise)

        # Challenge_titleのSubmitを取得
        submit_list = []
        for c in challenge:
            submit_list += SubmitModel.objects.filter(challenge_title=c)
        return submit_list

    # id=pkのExerciseを取得
    def get_context_data(self, **kwargs: Any) -> Any:
        context = super().get_context_data(**kwargs)
        context['exercise_detail'] = ExerciseModel.objects.get(pk=self.kwargs['pk'])
        return context