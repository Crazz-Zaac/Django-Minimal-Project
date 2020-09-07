from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from autos.models import Auto, Make
# from autos.forms import MakeForm

class MainView(LoginRequiredMixin, View):
	def get(self, request):
		mc = Make.objects.all().count();
		al = Auto.objects.all();

		ctx = {'make_count':mc, 'auto_list':al};
		return render(request, 'autos/auto_list.html', ctx)

#for 'make' model
class MakeView(LoginRequiredMixin, View):
	def get(self, request):
		ml = Make.objects.all();
		ctx = {'make_list':ml};
		return render(request, 'autos/make_list.html', ctx)

class MakeCreate(LoginRequiredMixin, CreateView):
	model = Make
	fields = '__all__'
	success_url = reverse_lazy('autos:all')

class MakeUpdate(LoginRequiredMixin, UpdateView):
	model = Make
	fields = '__all__'
	# template_name_suffix = '_'
	success_url = reverse_lazy('autos:all')

class MakeDelete(LoginRequiredMixin, DeleteView):
	model = Make
	fields = '__all__'
	template_name_suffix = '_confirm_delete'
	success_url = reverse_lazy('autos:all')

#for auto model
class AutoCreate(LoginRequiredMixin, CreateView):
	model = Auto
	fields = '__all__'
	success_url = reverse_lazy('autos:all')

class AutoUpdate(LoginRequiredMixin, UpdateView):
	model = Auto
	fields = '__all__'
	success_url = reverse_lazy('autos:all')

class AutoDelete(LoginRequiredMixin, DeleteView):
	model = Auto
	fields = '__all__'
	template_name_suffix = '_confirm_delete'
	success_url = reverse_lazy('autos:all')


