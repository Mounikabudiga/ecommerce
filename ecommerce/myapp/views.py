from django.shortcuts import render,redirect,HttpResponse
# Create your views here.
from .models import product_field,user_field,buyer


def products(request):
	if request.method == "POST":
		name = request.POST['name']
		description = request.POST['description']
		cost = request.POST['cost']
		noofproducts= request.POST['noofproducts']
		product_field.objects.create(name=name,description=description,cost=cost,noofproducts=noofproducts)
		return redirect('data')
	return render(request,'product.html')


def data(request):
	buyed=product_field.objects.all()
	return render(request,'data.html',{'details':buyed})

def destroy(request,id):
	data = product_field.objects.get(id=id)
	data.delete()
	return redirect('data')

def single(request,id):
	data = product_field.objects.get(id=id)
	if request.method=="POST":
		email=request.POST['email']
		data1 = user_field.objects.get(email=email)
		print(data1.account_bln)
		if data1.account_bln>0:
			data1.account_bln = data1.account_bln-data.cost
			data1.save()
			return render(request,'single_user.html',{'details':data1})
		else:
			return HttpResponse("Doesnt have sufficent money!")
			
	return render(request,'single.html',{'details':data})

def single_user(request,id):
	data = user_field.objects.get(id=id)
	return render(request,'single_user.html',{'details':data})


def user(request):
	if request.method=="POST":
		username=request.POST['username']
		email=request.POST['email']
		phone_no=request.POST['phone_no']
		account_bln=request.POST['account_bln']
		user_field.objects.create(username=username,email=email,phone_no=phone_no,account_bln=account_bln)
		return redirect('data1')
	return render(request,'user.html')


def data1(request):
	buyed=user_field.objects.all()
	return render(request,'data1.html',{'details':buyed})








