from django.shortcuts import render
from django.views import View

from .forms import LoginForm


class Login(View):
    form_class = LoginForm
    template_name = 'LoginApp/login.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class
        return render(request, self.template_name, {'form': form})
