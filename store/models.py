from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100,null=False)
    description = models.TextField(max_length=6000,null=False)
    price = models.IntegerField(default=0,null=False)
    image = models.ImageField(upload_to="uploads")
    file =  models.FileField(upload_to="uploads/files",null=False,default="")
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_available = models.BooleanField(default=True)

    @staticmethod
    def get_allproducts_by_category(category_id):
        if category_id:
            return Product.objects.filter(category=category_id,is_available=True)
        else:
            return Product.object.all()      


    def __str__(self):
        return self.name



class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=100,default=True)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=500)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zipcode = models.IntegerField(default=0)

    def __str__(self):
        return str(self.customer_id)+" - "+self.customer_name

class Payment(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date  = models.DateTimeField(auto_now_add=True)
    status_choice={
        ("SUCCESS","SUCCESS"),
        ("FAIL","FAIL")
    }
    status = models.CharField(choices=status_choice,max_length=40)
    customer_name = models.CharField(max_length=50,null=False,default=True)
    price = models.IntegerField(default=0,null=False)
    payment_id = models.CharField(max_length=100,null=True,blank=True)
    order_id = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.product.name

class Userproduct(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment,on_delete=models.CASCADE)
    order_status = models.CharField(max_length=100,null=True,blank=True)
    price = models.IntegerField(default=0,null=True)
    customer_name = models.CharField(max_length=50,null=True,default=True)


    def __str__(self):
        return self.product.name       

class SoldBook(models.Model):
    sold_id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)
    book_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    bookimage =  models.ImageField(upload_to="uploads")
    description = models.TextField(max_length=6000,null=False,default=True)


    def __str__(self):
        return str(self.sold_id)+" - "+self.book_name
