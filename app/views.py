from django.shortcuts import render,redirect
from .models import User,Product,Customer,OrderPlaced,Cart
from .forms import  CustomerRegistrationForm
from django.views import View
from django.contrib import messages
from django.views import View

def home(request):
 return render(request, 'app/home.html')

# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailView(View):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        return render(request,'app/productdetail.html',{'product':product})

class ProductView(View):
    def get(self,request):
        topwears = Product.objects.filter(category='TW')
        bottomwears = Product.objects.filter(category='BW')
        laptop = Product.objects.filter(category='L')
        mobile = Product.objects.filter(category='M')
        context ={'topwears':topwears,'bottomwears':bottomwears,'laptop':laptop,'mobile':mobile}
        return render(request,'app/home.html',{'topwears':topwears,'bottomwears':bottomwears,'mobile':mobile,'laptop':laptop})
        

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')

def admin_upload(request):
    if request.method =="POST" and request.FILES:
        title = request.POST['title']
        selling_p = request.POST['selling_price']
        discount_p = request.POST['discount_price']
        description = request.POST['description']
        brand = request.POST['brand']
        category = request.POST['category']
        product_img = request.FILES ['product_img']

        Pdt = Product(title=title,selling_price=selling_p,discount_price=discount_p,
        description=description,brand=brand,category=category,product_img=product_img)
        Pdt.save()
        return redirect('/')

    return render(request,'app/admin.html')


class  CustomerRegistrationView(View):
    def get(self,request):
        form =  CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',
        {'form':form})
    def post(self,request):
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'successfully registerd')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})