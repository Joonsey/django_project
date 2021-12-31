from django.urls import path
from . import views


# Create your views here.
urlpatterns = [
    path('', views.home, name='portfolio-home')
]
from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)