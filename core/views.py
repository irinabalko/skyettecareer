from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
import core.models as coremodels

# Create your views here.

class LandingView(TemplateView):
	template_name = "base/index.html"


class WorkplaceListView(ListView):
	model = coremodels.Workplace	
	template_name = 'workplace/list.html'

class SearchListView(WorkplaceListView):

	def get_queryset(self):
		incoming_query_string = self.request.GET.get('query', '')
		return coremodels.Workplace.objects.filter(title__icontains=incoming_query_string)

class WorkplaceDetailView(DetailView):
	model = coremodels.Workplace	
	template_name = 'workplace/detail.html'	
	context_object_name = 'workplace'

	def get_context_data(self,**kwargs):
		context = super(WorkplaceDetailView, self).get_context_data(**kwargs)
		workplace = coremodels.Workplace.objects.get(id=self.kwargs['pk'])
		if self.request.user.is_authenticated():
			user_reviews = coremodels.Review.objects.filter(workplace=workplace, user=self.request.user)
			if user_reviews.count() > 0:
				context['user_review'] = user_reviews[0]
			else:
				context['user_review'] = None

		return context

class WorkplaceCreateView(CreateView):
	model = coremodels.Workplace
	template_name = 'base/form.html'	
	fields = "__all__"

class WorkplaceUpdateView(UpdateView):
	model = coremodels.Workplace
	template_name = 'base/form.html'
	fields = "__all__"	

class ReviewCreateView(CreateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields = ['description', 'overall', 'paid_parental_leave', 'female_rolemodels', 'salary', 'flexible_hours', 'telecommuting', 'equal_opportunities']

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.workplace = coremodels.Workplace.objects.get(id=self.kwargs['pk'])
		return super(ReviewCreateView, self).form_valid(form)

	def get_success_url(self):
		return self.object.workplace.get_absolute_url()	

class ReviewUpdateView(UpdateView):
	model = coremodels.Review
	template_name = 'base/form.html'
	fields = ['description', 'overall', 'paid_parental_leave', 'female_rolemodels', 'salary', 'flexible_hours', 'telecommuting', 'equal_opportunities']

	def get_object(self):
		return coremodels.Review.objects.get(workplace__id=self.kwargs['pk'], user=self.request.user)

	def get_success_url(self):
		return self.object.workplace.get_absolute_url()	
	
		