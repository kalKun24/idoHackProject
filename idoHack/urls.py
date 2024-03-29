from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('', include('challenge.urls')),
    path('', include('account.urls')),
    path('', include('infomation.urls')),
    path('admin/', admin.site.urls),
    path('mededitor/', include('mdeditor.urls')),

]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
