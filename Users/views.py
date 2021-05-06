from django.shortcuts import render, HttpResponse
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import UserRegisterForm


class UserSignup(CreateView):
    template_name = 'signup.html'
    success_url = reverse_lazy('login')
    form_class = UserRegisterForm


class UserLogin(LoginView):
    template_name = 'signin.html'


class UserEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'is_superuser']
    success_url = reverse_lazy('index')
    template_name = 'user_edit.html'

    def test_func(self):
        return self.request.user.is_superuser


class UserList(ListView):
    model = User
    template_name = 'users_list.html'

    def test_func(self):
        return self.request.user.is_superuser


class UserDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = User
    success_url = reverse_lazy('index')
    template_name = 'user_confirm_delete.html'

    def test_func(self):
        return self.request.user.is_superuser
