from django.urls import path, include
from django.views.generic import RedirectView

from News import views

urlpatterns = [
    path('', RedirectView.as_view(url='main/', permanent=True), name='index'),
    path('main/', include('News.urls')),
    path('exams/', include('Exams.urls')),
]
