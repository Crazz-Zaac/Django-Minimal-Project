from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import View
from cats.models import Cat, Breed

class CatList(LoginRequiredMixin, View):
	def get(self, request):
		cnt = Breed.objects.all().count();
		lst = Cat.objects.all();

		ctx = {'breed_count':cnt, 'cat_list':lst}; #a dictionary of breed_count and cat_list
		return render(request, 'cats/cat_list.html', ctx)

#There must be breed to add cats. So we must 
class BreedView(LoginRequiredMixin, View):
	def get(self, request):
		ml = Breed.objects.all();
		ctx = {'breed_list':ml};
		return render(request, 'cats/breed_list.html', ctx)

class BreedCreate(LoginRequiredMixin, CreateView):
	model = Breed
	fields = '__all__'
	success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
	model = Breed
	fields = '__all__'
	success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
	model = Breed
	fields = '__all__'
	template_name_suffix = '_confirm_delete'
	success_url = reverse_lazy('cats:all')


#only when breed is there we can add Cats 
class CatCreate(LoginRequiredMixin, CreateView):
	model = Cat
	fields = '__all__'
	success_url = reverse_lazy('cats:all')


class CatUpdate(LoginRequiredMixin, UpdateView):
	model = Cat
	fields = '__all__'
	success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
	model = Cat
	fields = '__all__'
	template_name_suffix = '_confirm_delete'
	success_url = reverse_lazy('cats:all')

