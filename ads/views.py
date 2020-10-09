from ads.models import Ad, Comment, Fav
from ads.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.views import View 
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse
from ads.forms import CreateForm, CommentForm
from ads.utils import dump_queries
from django.db.models import Q
from django.contrib.humanize.templatetags.humanize import naturaltime

class AdListView(OwnerListView):
	model = Ad
	#By convention:
	#template_name = "ads/ad_list.html"
	def get(self, request):
		strval  = request.GET.get("search", False)
		ad_list = Ad.objects.all()
		favorites = list()

		if request.user.is_authenticated:
			rows = request.user.favorite_ads.values('id')
			favorites = [ row['id'] for row in rows]
		
		if strval:
			#For simple title-only search
			#objects = Post.objects.filter(title_contains=strval).select_related().order_by('-updated_at')[:10]

			#For multi-field search
			query = Q(title__contains=strval)
			query.add(Q(text__contains=strval), Q.OR)
			objects = Ad.objects.filter(query).select_related().order_by('-updated_at')[:10]
		else:
			objects = Ad.objects.all().order_by('-updated_at')[:10]
			#objects = Post.objects.select_related().all().order_by('-updated_at').[:10]

		for obj in objects:
			obj.natural_updated = naturaltime(obj.updated_at)


		ctx = {'ad_list': objects, 'search':strval, 'favorites': favorites}
		retval = render(request, 'ads/ad_list.html', ctx)

		dump_queries()
		return retval

class AdDetailView(OwnerDetailView):
	model = Ad

	def get(self, request, pk):
		a = Ad.objects.get(id=pk)
		comments = Comment.objects.filter(ad=a).order_by('-updated_at')
		comment_form = CommentForm()
		context = {'ad': a, 'comments':comments, 'comment_form':comment_form}
		return render(request, 'ads/ad_detail.html', context)

class AdCreateView(LoginRequiredMixin, View):
	# model = Ad
	# fields = ['title', 'price', 'text']
	success_url = reverse_lazy('ads:all')

	def get(self, request, pk=None):
		form = CreateForm()
		ctx = {'form': form}
		return render(request, 'ads/ad_form.html', ctx)

	def post(self, request, pk=None):
		form = CreateForm(request.POST, request.FILES or None)

		if not form.is_valid():
			ctx = {'form': form}
			return render(request, 'ads/ad_form.html', ctx)
		
		#Add owner to the model before saving		
		pic = form.save(commit=False)
		pic.owner = self.request.user
		pic.save()
		return redirect(self.success_url)


class AdUpdateView(LoginRequiredMixin, View):
	# model = Ad
	# fields = ['title', 'price', 'text']
	success_url = reverse_lazy('ads:all')

	def get(self, request, pk):
		pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
		form = CreateForm(instance=pic)
		ctx = {'form': form}
		return render(request, 'ads/ad_form.html', ctx)

	def post(self, request, pk=None):
		pic = get_object_or_404(Ad, id=pk, owner=self.request.user)
		form = CreateForm(request.POST, request.FILES or None, instance=pic)

		if not form.is_valid():
			ctx = {'form': form}
			return render(request, 'ads/ad_form.html', ctx)

		pic = form.save(commit=False)
		pic.save()

		return redirect(self.success_url)


class AdDeleteView(OwnerDeleteView):
	model = Ad


def stream_file(request, pk):
	pic = get_object_or_404(Ad, id=pk)
	response = HttpResponse()
	response['Content-Type'] = pic.content_type
	response['Content-Length'] = len(pic.picture)
	response.write(pic.picture)
	return response


class CommentCreateView(LoginRequiredMixin, View):
	def post(self, request, pk):
		ad = get_object_or_404(Ad, id=pk)
		comment = Comment(text=request.POST['comment'], owner=request.user, ad=ad)
		comment.save()
		return redirect(reverse('ads:ad_detail', args=[pk]))

class CommentDeleteView(OwnerDeleteView):
	model = Comment
	template_name = "ads/comment_delete.html"

	def get_success_url(self):
		ad = self.object.ad
		return reverse('ads:ad_detail', args=[ad.id])


from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
	def post(self, request, pk):
		print("Add PK", pk)
		ad = get_object_or_404(Ad, id=pk)
		fav = Fav(user=request.user, ad=ad)
		try:
			fav.save() #instead of duplicate key
		except IntegrityError as e:
			pass
		return HttpResponse()


@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
	def post(self, request, pk):
		print("Delete PK", pk)
		ad = get_object_or_404(Ad, id=pk)
		try:
			fav = Fav.objects.get(user=request.user, ad=ad).delete()
		except Fav.DoesNotExist as e:
			pass

		return HttpResponse()


# References

# https://docs.djangoproject.com/en/3.0/topics/db/queries/#one-to-many-relationships

# Note that the select_related() QuerySet method recursively prepopulates the
# cache of all one-to-many relationships ahead of time.

# sql “LIKE” equivalent in django query
# https://stackoverflow.com/questions/18140838/sql-like-equivalent-in-django-query

# How do I do an OR filter in a Django query?
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query

# https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running