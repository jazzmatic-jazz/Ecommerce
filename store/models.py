from django.db import models
from datetime import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    @staticmethod
    def get_all_categories():
        return category.objects.all()
    
    class Meta:
        verbose_name_plural = 'categories'
    
    def __str__(self):
        return self.name

class Customer(models.Model):
    first_name = models.CharField('Customer\'s First name:', max_length=50)
    last_name = models.CharField('Customer\'s Last name:', max_length=50)
    phone = models.CharField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length = 10)

    #to save the data
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        
        except:
            return False
    
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        
        return False
    
    def __str__(self):
        return self.first_name
    

class Product(models.Model):
    name =  models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey("Category", verbose_name="Product Category", on_delete=models.CASCADE)
    description = models.CharField(default="", max_length=250, blank=True, null= True)
    image = models.ImageField( upload_to='static\product')

    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.get(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_product_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    customer = models.ForeignKey("Customer", on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    address =  models.CharField(default="", max_length=50, blank=True)
    date = models.DateField(auto_now=True, auto_now_add=False)
    status =  models.BooleanField(default=False)

    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_order_by_customer(customer_id):
        return Order.Objects.filter(customer=customer_id).order_by('-date')

    def __str__(self):
        return self.product
