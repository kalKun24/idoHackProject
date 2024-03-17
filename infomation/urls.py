from django.urls import path
from . import views

urlpatterns = [
    path('FAQ/', views.FAQView.as_view(), name='faq'),
]
