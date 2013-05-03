# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from django.template import RequestContext
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from models import *
from forms import *
def index_view(request):
    t = get_template('menu/index1.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
def login_view(request):
#    if request.user.is_active:
#        return HttpResponse('<script>alert("you are already login");top.location="/menu/list/";</script>')
    if request.user.is_authenticated():
        return HttpResponse('<script>alert("you are already login");top.location="/menu/list/";</script>')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponse('<script>alert("login success!");top.location="/menu/list/";</script>')
            else:
                return HttpResponse('<script>alert("login error!");top.location="/menu/lggin/";</script>')
        else:
            return HttpResponse('<script>alert("User None!");top.location="/menu/login/";</script>')

    t = get_template('menu/login.html')
    c = RequestContext(request, locals())
    return HttpResponse(t.render(c))
@login_required
def logout_view(request):
    logout(request)
    return HttpResponse('<script>alert("logout success!");top.location="/menu/accounts/login/";</script>')
@login_required
def create_dish(request):
    form = DishForm()
    if request.method == 'POST':
        form = DishForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<script>alert("ok");top.location="/menu/list/";</script>')
    else:
        t = get_template('menu/create_dish.html')
        c = RequestContext(request, locals())
        return HttpResponse(t.render(c))
@login_required
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
@login_required
def view_bill(request):
    bill = request.session.get(bill,None)
    t = get_template('menu/view_bill.html')

    if not bill:
        bill = bill()
        request.session["bill"] = bill

        c = RequestContext(request,locals())
        return HttpResponse(t.rande(c))
def edit_dish(request, id):
    dish_instance = Dish.objects.get(id=id)
    form = DishForm(request.POST or request.FILES or None, instance = dish_instance)
    if form.is_valid():
        form.save()
        return HttpResponse('<script>alert("edit success!");top.location="/menu/list/";</script>')
    t=get_template('menu/edit_dish.html')
    c=RequestContext(request,locals())
    return HttpResponse(t.render(c))
