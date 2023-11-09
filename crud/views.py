from django.shortcuts import render, redirect
from . models import Product

# Create your views here.
def home(request):
	all_product = Product.objects.all().order_by('-created_at')
	return render(request, 'crud/home.html', {'product': all_product})

def add_product(request):
	if request.method == 'POST':
		if request.POST.get('product')\
			and request.POST.get('purchase')\
			and request.POST.get('sale')\
			and request.POST.get('qty')\
			and request.POST.get('gender')\
			or request.POST.get('note'):
			product = Product()
			product.product = request.POST.get('product')
			product.purchase = request.POST.get('purchase')
			product.sale = request.POST.get('sale')
			product.qty = request.POST.get('qty')
			product.gender = request.POST.get('gender')
			product.note = request.POST.get('note')
			product.save()
			return redirect('/')
	else:
		return render(request, 'crud/add.html', {})		

def product(request, product_id):
	product = Product.objects.get(id = product_id)
	if product != None:
		return render(request, 'crud/edit.html', {'product': product})


def edit_product(request):
	if request.method == 'POST':
		product = Product.objects.get(id = request.POST.get('id'))
		if product != None:

			product.product = request.POST.get('product')
			product.purchase = request.POST.get('purchase')
			product.sale = request.POST.get('sale')
			product.qty = request.POST.get('qty')
			product.gender = request.POST.get('gender')
			product.note = request.POST.get('note')
			product.save()
			return redirect('/')


def delete_product(request):
	product = Product.objects.get(id = product_id)
	product.delete()
	return redirect('/')					