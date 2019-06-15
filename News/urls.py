from django.urls import path
from django.views.generic import RedirectView

from News.views import ListNewsView, DeleteNewsView, UpdateNewsView, CreateNewsView

urlpatterns = [
    path('', RedirectView.as_view(url='list/', permanent=True)),
    path('list/', ListNewsView.as_view(), name='MainPage'),
    path('delete/<pk>', DeleteNewsView.as_view(), name='DeleteNews'),
    path('update/<pk>', UpdateNewsView.as_view(), name='UpdateNews'),
    path('create/', CreateNewsView.as_view(), name='CreateNews'),
]
