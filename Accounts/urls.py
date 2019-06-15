from django.urls import path
from .views import RegisterView, LoginView, ProfileView, ChangePasswordView, LogOutView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='Register'),
    path('login/', LoginView.as_view(), name='Login'),
    path('logout/', LogOutView.as_view(), name='LogOut'),
    path('profile/', ProfileView.as_view(), name='Profile'),
    path('changePassword/', ChangePasswordView.as_view(), name='ChangePassword'),
]
