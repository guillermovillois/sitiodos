from django.shortcuts import render, get_object_or_404
import random
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from .models import RestaurantLocation
from django.db.models import Q
from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#@login_required()
class RestaurantCreateView(LoginRequiredMixin, CreateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name='form.html'
	#success_url='/restaurants/'
	def form_valid(self, form):
		instance = form.save(commit=False)
		instance.owner = self.request.user
		return super(RestaurantCreateView, self).form_valid(form)
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantCreateView, self).get_context_data(*args,**kwargs)
		context['title'] = 'Add Restaurant'
		return context

class RestaurantUpdateView(LoginRequiredMixin, UpdateView):
	form_class = RestaurantLocationCreateForm
	login_url = '/login/'
	template_name='restaurants/detail-update.html'
	def get_context_data(self, *args, **kwargs):
		context = super(RestaurantUpdateView, self).get_context_data(*args,**kwargs)
		name = self.get_object().name
		context['title'] = f'Update Restaurant: {name}'
		return context
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)


def restaurant_createview(request):
	form = RestaurantLocationCreateForm(request.POST or None)
	errors = None
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/restaurants')
	if form.errors:
		errors = form.errors
	template_name='restaurants/form.html'
	context = {'form':form, 'errors':errors}
	return render(request, template_name, context)

def restaurant_listview(request):
	template_name='restaurants/restaurants_list.html'
	queryset = RestaurantLocation.objects.all()
	context = {
		'object_list':queryset
	}
	return render(request, template_name, context)

class RestaurantListView(LoginRequiredMixin, ListView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)
		# slug = self.kwargs.get('slug')
		# if slug:
		# 	queryset = RestaurantLocation.objects.filter(
		# 		Q(category__iexact=slug),
		# 		Q(category__icontains=slug)
		# 		)
		# else:
		# 	queryset = RestaurantLocation.objects.all()
		# return queryset

class RestaurantDetailView(LoginRequiredMixin,DetailView):
	def get_queryset(self):
		return RestaurantLocation.objects.filter(owner=self.request.user)


# class MexicanRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact='mexican')
# 	template_name='restaurants/restaurants_list.html'

# class PizzaRestaurantListView(ListView):
# 	queryset = RestaurantLocation.objects.filter(category__iexact='pizza')
# 	template_name='restaurants/restaurants_list.html'
# Create your views here.
# def home(request):
# 	jota1 = 'soy el mejor'
# 	num = random.randint(0, 10000000)
# 	some_list = [num, random.randint(0, 10000000), random.randint(0, 10000000)]
# 	context = {
# 		'jota':jota1, 
# 		'randomnumber': num, 
# 		'some_list': some_list
# 	}
# 	return render(request, 'base.html', context)

# def about(request):
# 	context = {

# 	}
# 	return render(request, 'about.html', context)

# def contact(request):
# 	context = {

# 	}
# 	return render(request, 'contact.html', context)

# class ContactView(View):
# 	def get(self, request, *args, **kwargs):
# 		print(kwargs)
# 		context = {}
# 		return render(request, 'contact.html', context)

# class HomeTemplateView(TemplateView):
# 	template_name = 'base.html'
# 	def get_context_data(self, *args, **kwargs):
# 		jota1 = 'soy el mejor'
# 		num = random.randint(0, 10000000)
# 		some_list = [num, random.randint(0, 10000000), random.randint(0, 10000000)]
# 		context = {
# 			'jota':jota1, 
# 			'randomnumber': num, 
# 			'some_list': some_list
# 		}
# 		return context

# class AboutTemplateView(TemplateView):
# 	template_name = 'about.html'

# class ContactTemplateView(TemplateView):
# 	template_name = 'contact.html'