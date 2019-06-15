# Create your views here.
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView, UpdateView
from django.views.generic.base import View

from Accounts.forms import UserCreateForm, UserLoginForm, UserProfileForm, ChangePasswordForm
from Accounts.models import RExamUserModel
from RExam.mixins import NotAuthCheckMixin


class RegisterView(NotAuthCheckMixin, CreateView):
    model = RExamUserModel
    template_name = 'Accounts/RegisterFormTemplate.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('Login')


class LoginView(NotAuthCheckMixin, FormView):
    form_class = UserLoginForm
    template_name = 'Accounts/LoginFormTemplate.html'
    success_url = reverse_lazy('MainPage')

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        return super(LoginView, self).form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'Accounts/ProfileFormTemplate.html'
    success_url = reverse_lazy('Profile')
    form_class = UserProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        post = form.save(commit=False)
        post.username = self.request.user.username
        post.save()
        return super(ProfileView, self).form_valid(form)


class ChangePasswordView(LoginRequiredMixin, UpdateView):
    template_name = 'Accounts/ChangePasswordTemplate.html'
    success_url = reverse_lazy('MainPage')
    model = RExamUserModel
    form_class = ChangePasswordForm

    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial(),
                  'user': self.request.user}
        if self.request.method == 'POST':
            kwargs.update({
                'user': self.request.user,
                'data': self.request.POST,
            })
        return kwargs

    def get_object(self, queryset=None):
        return self.request.user


class LogOutView(LoginRequiredMixin, View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('Login'))
