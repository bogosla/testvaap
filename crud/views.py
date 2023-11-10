from django.shortcuts import render, redirect
from . models import Product
from django.db.models import F, ExpressionWrapper, DecimalField, Sum

# Create your views here.
def home(request):
	all_product = Product.objects.annotate(amount=ExpressionWrapper(F('purchase') * F('qty'), output_field=DecimalField())).all().order_by('-created_at')
	total = all_product.aggregate(total=Sum("amount"))["total"]
	return render(request, 'crud/home.html', {'products': all_product, 'total': total})

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
			product.note = request.POST.get('note', None)
			product.save()
			return redirect('/')
	else:
		return render(request, 'crud/add.html', {})		

def product(request, product_id):
	product = Product.objects.get(pk=product_id)
	if product != None:
		return render(request, 'crud/edit.html', {'product': product})


def edit_product(request):
	if request.method == 'POST':
		product = Product.objects.get(pk=request.POST.get('id'))
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
	if request.method == "POST":
		product_id = request.POST["product_id"]
		product = Product.objects.get(pk=product_id)
		product.delete()
	return redirect('/')					