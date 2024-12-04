from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  # Шаблон для отображения формы входа
    success_url = reverse_lazy('home')  # URL для перенаправления после успешного входа


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('goodbye')  # URL для перенаправления после выхода из системы


class RegisterView(CreateView):
    template_name = 'register.html'
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('home')