from django.urls import path

from Exams import views

urlpatterns = [
    path('list/', views.ExamsListView.as_view(), name='ListExams'),
    path('create/', views.ExamCreateView.as_view(), name='CreateExam'),
]
