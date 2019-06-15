from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy


class NotAuthCheckMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse_lazy('MainPage'))
        return super(NotAuthCheckMixin, self).dispatch(request, *args, **kwargs)
