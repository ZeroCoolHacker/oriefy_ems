from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.views.generic import CreateView, DetailView
from employee.models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from employee.forms import BasicEmployeeCreateForm


# Create your views here.
class EmployeeCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    """
    View that creates an employee entry
    """
    permission_denied_message = 'You are not logged in. Kindly log in with your company provided username'
    template_name_suffix = '_create_form'
    message = 'Basic Information Complete'
    form_class = BasicEmployeeCreateForm
    model = Employee


    def test_func(self):
        if Employee.objects.filter(user=self.request.user).count() is not 0:
            return False
        else:
            return True
    

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.verified = False
        print(form.instance)
        return super().form_valid(form)

    def get_success_url(self):
        messages.success(self.request, self.message)
        return reverse('employee:profile', kwargs={'pk':self.request.user.pk})


class EmployeeDetailView(LoginRequiredMixin, DetailView):
    """Basic DetailView implementation to call an individual article."""
    model = Employee

