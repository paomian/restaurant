# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse

from models import *
from forms import *




def create_dish(request):
	form = DishForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DishForm()

	t = get_template('menu/create_dish.html')
	c = RequestContext(request,locals())
	return HttpResponse(t.render(c))
