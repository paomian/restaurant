# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
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
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))
def list_dish(requset):
    list_item = dish.objects.all()
    paginator = Paginator(list_item, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_item = paginator.page(page)
    except:
        list_item = paginator.page(paginator,num_pages)

    t = get_template('menu/list_dish.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
