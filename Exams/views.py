# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from Exams.forms import ExamCreateForm
from Exams.models import ExamModel


class ExamsListView(ListView):
    model = ExamModel
    ordering = ['-date']
    paginate_by = 10
    template_name = 'Exams/ListExamsTemplate.html'


class ExamCreateView(CreateView):
    model = ExamModel
    form_class = ExamCreateForm
    success_url = reverse_lazy('ListExams')
    template_name = 'Exams/CreateExamTemplate.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super(ExamCreateView, self).form_valid(form)
