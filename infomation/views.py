from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import InfomationModel, FrequentlyAskedQuestionModel

# Create your views here.
class FAQView(ListView):
    model = FrequentlyAskedQuestionModel
    template_name = 'infomation/faq.html'
    context_object_name = 'faq_list'