# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from models import *
from forms import *

def user_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username,password=password)
    if user is not None:
        if user.is_active:
            login(request,user)
            print "login success!"
        else:
            print "login error!"
    else:
        print "User None!"

def logout_view(request):
    logout(request)
    print "logout secccess!"
def create_dish(request):
	form = DishForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = DishForm()

	t = get_template('menu/create_dish.html')
	c = RequestContext(request, locals())
	return HttpResponse(t.render(c))
def list_dish(request):
    list_items = Dish.objects.all()
    paginator = Paginator(list_items, 10)

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    try:
        list_items = paginator.page(page)
    except:
        list_items = paginator.page(paginator,num_pages)

    t = get_template('menu/list_dish.html')
    c = RequestContext(request,locals())
    return HttpResponse(t.render(c))
def view_bill(request):
    bill = request.session.get(bill,None)
    t = get_template('menu/view_bill.html')

    if not bill:
        bill = bill()
        request.session["bill"] = bill

        c = RequestContext(request,locals())
        return HttpResponse(t.rande(c))
