from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import core.models as coremodels

# Create your views here.

class LandingView(TemplateView):
	template_name = "base/index.html"


class WorkplaceListView(ListView):
	model = coremodels.Workplace	
	template_name = 'workplace/list.html'


class WorkplaceDetailView(DetailView):
	model = coremodels.Workplace	
	template_name = 'workplace/detail.html'	
	context_object_name = 'workplace'