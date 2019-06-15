# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from News.forms import AddNewsForm, UpdateNewsForm
from News.models import NewsModel


class ListNewsView(LoginRequiredMixin, ListView):
    model = NewsModel
    paginate_by = 2
    template_name = 'News/ListNewsTemplate.html'


class DeleteNewsView(PermissionRequiredMixin, DeleteView):
    model = NewsModel
    success_url = reverse_lazy('MainPage')
    permission_required = 'News.delete_news'


class UpdateNewsView(PermissionRequiredMixin, UpdateView):
    model = NewsModel
    success_url = reverse_lazy('MainPage')
    permission_required = 'News.change_news'
    template_name = 'News/NewsUpdateFormTemplate.html'
    form_class = UpdateNewsForm


class CreateNewsView(PermissionRequiredMixin, CreateView):
    model = NewsModel
    success_url = reverse_lazy('MainPage')
    permission_required = 'News.add_news'
    template_name = 'News/NewsCreateFormTemplate.html'
    form_class = UpdateNewsForm

    def form_valid(self, form):
        post = form.save(commit=False)
        post.author = self.request.user
        return super(CreateNewsView, self).form_valid(form)
