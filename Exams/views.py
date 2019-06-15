# Create your views here.
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, DeleteView

from Exams.forms import ExamCreateForm, QuestionCreateForm
from Exams.models import ExamModel, QuestionModel


class ExamsListView(ListView):
    model = ExamModel
    ordering = ['-date']
    paginate_by = 10
    template_name = 'Exams/ListExamsTemplate.html'


class ExamCreateView(PermissionRequiredMixin, CreateView):
    model = ExamModel
    form_class = ExamCreateForm
    success_url = reverse_lazy('ListExams')
    template_name = 'Exams/CreateExamTemplate.html'
    permission_required = 'Exams.add_exammodel'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super(ExamCreateView, self).form_valid(form)


class ExamDetailView(DetailView):
    model = ExamModel
    template_name = 'Exams/DetailExamTemplate.html'

    def get_context_data(self, **kwargs):
        context = super(ExamDetailView, self).get_context_data(**kwargs)
        try:
            context['questions'] = QuestionModel.objects.filter(exam=self.kwargs['pk'])
        except ObjectDoesNotExist:
            context['questions'] = None
        return context


class QuestionCreateView(PermissionRequiredMixin, CreateView):
    model = QuestionModel
    form_class = QuestionCreateForm
    template_name = 'Exams/CreateQuestionTemplate.html'
    permission_required = 'Exams.add_questionmodel'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.exam = get_object_or_404(ExamModel, pk=self.kwargs.get('pk'))
        return super(QuestionCreateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('DetailExam', kwargs={'pk': self.kwargs['pk']})


class QuestionDeleteView(PermissionRequiredMixin, DeleteView):
    model = QuestionModel
    permission_required = 'Exams.delete_questionmodel'

    def get_success_url(self):
        return reverse('DetailExam', kwargs={'pk': self.kwargs['exam_id']})
