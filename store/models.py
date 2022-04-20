from django.db import models

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