from django.urls import path

from Exams import views

urlpatterns = [
    path('list/', views.ExamsListView.as_view(), name='ListExams'),
    path('create/', views.ExamCreateView.as_view(), name='CreateExam'),
    path('detail/<pk>', views.ExamDetailView.as_view(), name='DetailExam'),
    path('question/create/<pk>', views.QuestionCreateView.as_view(), name='QuestionCreate'),
    path('question/delete/<pk>?exam_id=<exam_id>', views.QuestionDeleteView.as_view(), name='QuestionDelete'),
    path('question/detail/<pk>', views.QuestionDetailView.as_view(), name='QuestionDetail'),
    path('remove/<pk>', views.ExamRemoveView.as_view(), name='ExamRemove'),
    path('update/<pk>', views.ExamUpdateView.as_view(), name='ExamUpdate'),
]
