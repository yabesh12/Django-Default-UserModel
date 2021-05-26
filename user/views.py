from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from user.forms import UserForm


def home(request):
	count = User.objects.count()
	context= {'count': count}
	return render(request, 'registration/home.html', context)


def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'Account created successfully')
			return redirect('home')
	else:
		form = UserCreationForm()
	context = {'form': form}
	return render(request, 'registration/signup.html', context)


@login_required
def secret_page(request):
	return render(request, 'registration/secret_page.html')


class SecretPage(LoginRequiredMixin, TemplateView):
	template_name = 'registration/secret_page.html'
