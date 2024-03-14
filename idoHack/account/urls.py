from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', views.LogoutView, name='logout'),
    path('signup', views.SignupView.as_view(), name='signup'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)