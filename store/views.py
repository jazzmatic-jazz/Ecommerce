from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import Product, Category, Order, Customer
from django.views import View
from django.contrib.auth.hashers import check_password

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove =  request.POST.get('remove')
        cart = request.session.get('cart')

        if cart:
            quantity = cart.get(product)
            
            if quantity:
                if remove:
                    if quantity <= 1:
                        cart.pop(product)
                    
                    else:
                        cart[product] = quantity-1
                
                else:
                    cart[product] = quantity+1
                
            else:
                cart[product] = 1
        
        else:
            cart = {}
            cart[product] = 1
        
        request.session['cart'] = cart
        print('cart', request.session['cart'])
    
    def get(self, request):
        return HttpResponseRedirect(f'/store{request.get_full_path()[1:]}')
    

def store(request):
    cart = request.session.get('cart')

    if not cart:
        request.session['cart'] = {}
    
    product = None
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        product = Product.get_all_product_by_categoryid(categoryID)
    
    else:
        product = Product.objects.all()

    data = {}
    data['product'] = product
    data['categories'] = categories

    print ('You are:', request.session.get('email'))

    return render (request, 'index.html', data)

class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url= request.GET.get('return_url')
        return render(request,'login.html')
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None

        if customer:
            flag = check_password(password, customer.password)

            if flag:
                request.session['customer'] = customer.id

                if Login.return_url:
                    return HttpResponseRedirect(Login.return_url)
                
                else:
                    Login.return_url = None
                    return redirect('homepage')
            
            else:
                error_message = "Invalid!"
        
        else:
                error_message = "Invalid!"

        print(email,password)
        return render(request, 'login.html', {'error': error_message })


def logout(request):
    request.session.clear()
    return redirect('login')