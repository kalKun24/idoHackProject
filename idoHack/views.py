from django.shortcuts import render
from django.views.generic import ListView
from infomation.models import InfomationModel

class IndexView(ListView):
    model = InfomationModel
    template_name = 'index.html'
    context_object_name = 'infomation_list'
