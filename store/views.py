
from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from .utils import cookieCart, cartData, guestOrder
from .forms import RegistrationForm
from django.http import HttpResponseRedirect, request
from django.views.generic import ListView, DetailView
from store.models import Customer
from django.contrib import messages


def index(request):
    posts = Product.objects.all().order_by("-id")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/home.html', context)
def contact(request):
    return render(request, 'store/contact.html')
def error404(request,exception):
    return render(request, 'store/error.html')
def error500(request):
    return render(request, 'store/error.html')
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username= form.cleaned_data.get('username')
            Customer.objects.create(user=user, name=username)
           
            return HttpResponseRedirect('/')
    return render(request, 'store/register.html', {'form': form})

def vga(request):
    posts = Product.objects.filter(typePD='VGA').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)
def cpu(request):
    posts = Product.objects.filter(typePD='CPU').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def mainboard(request):
    posts = Product.objects.filter(typePD='Mainboard').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def ram(request):
    posts = Product.objects.filter(typePD='RAM').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def psu(request):
    posts = Product.objects.filter(typePD='PSU').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def case(request):
    posts = Product.objects.filter(typePD='Case').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def hdd(request):
    posts = Product.objects.filter(typePD='HDD').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def ssd(request):
    posts = Product.objects.filter(typePD='SSD').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def man_hinh(request):
    posts = Product.objects.filter(typePD='LCD').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def chuot(request):
    posts = Product.objects.filter(typePD='Mouse').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def ban_phim(request):
    posts = Product.objects.filter(typePD='Keyboard').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def tai_nghe(request):
    posts = Product.objects.filter(typePD='Headphone').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def ghe_gaming(request):
    posts = Product.objects.filter(typePD='Chair').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def phu_kien(request):
    posts = Product.objects.filter(typePD='Accessories').order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def item(request,slug):
    posts = Product.objects.filter(urlsPD=slug)
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(urlsPD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/item.html', context)


class SearchView(ListView):
    template_name = 'store/shop.html'
    context_object_name = 'posts'
    model = Product
    def get_queryset(self, *args, **kwargs):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Product.objects.filter(namePD__contains=query)
            result = postresult
        else:
            result = None
        return result



def store(request):
    posts = Product.objects.all().order_by("-prices")
    search_query = request.GET.get('q')
    if search_query:
        posts = posts.filter(
            Q(namePD__icontains = search_query) |
            Q(typesPD__icontains = search_query)
        )
    context={
        'posts': posts
    }
    return render(request, 'store/shop.html', context)

def cart(request):
	data = cartData(request)

	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	order = data['order']
	items = data['items']

	context = {'items':items, 'order':order, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)

	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)

	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		
		)

	return JsonResponse('Payment submitted..', safe=False)