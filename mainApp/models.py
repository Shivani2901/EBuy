from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    email_token =models.CharField(max_length=200)
    is_verified =models.BooleanField(default=False)

class Seller(models.Model):
    name=models.CharField(max_length=50)
    uname=models.CharField(max_length=20)
    email=models.EmailField(default=None,null=True,blank=True)
    phone=models.CharField(max_length=20,default=None,null=True,blank=True)
    bankName=models.CharField(max_length=20,default=None,null=True,blank=True)
    ifscCode=models.CharField(max_length=20,default=None,null=True,blank=True)
    accountNumber=models.CharField(max_length=20,default=None,null=True,blank=True)
    total=models.IntegerField(default=None,null=True,blank=True)

    def __str__(self):
        return str(self.id)+" "+self.name

class Buyer(models.Model):
    name = models.CharField(max_length=50)
    uname = models.CharField(max_length=20)
    email = models.EmailField(default=None, null=True, blank=True)
    phone = models.CharField(max_length=20)
    address1 = models.CharField(max_length=20)
    address2 = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+" "+self.name

class Category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.name


class Brand(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+" "+self.name
#
# class SubCategory(models.Model):
#     name=models.CharField(max_length=50)
#     category = models.ForeignKey(Category,on_delete=models.CASCADE)
#     def __str__(self):
#         return str(self.id)+" "+self.name

class Product(models.Model):
    stock= models.BooleanField(default=False)
    name = models.CharField(max_length=200)
    desc = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    # subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    basePrice = models.IntegerField()
    discount = models.IntegerField(default=0, null=True, blank=True)
    finalPrice = models.IntegerField(default=0, null=True, blank=True)
    size1 = models.CharField(max_length=10,default=None, null=True, blank=True)
    size2 = models.CharField(max_length=10,default=None, null=True, blank=True)
    size3 = models.CharField(max_length=10,default=None, null=True, blank=True)
    size4 = models.CharField(max_length=10,default=None, null=True, blank=True)
    size5 = models.CharField(max_length=10,default=None, null=True, blank=True)
    img1 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img2 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img3 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    img4 = models.ImageField(upload_to='images/', default=None, blank=True, null=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id) + "" + self.name

class Cart(models.Model):
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=10,default=None, null=True, blank=True)
    total = models.IntegerField()

    def __str__(self):
        return str(self.id)+" "+self.buyer.name

class Checkout(models.Model):
    # cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    buyer = models.ForeignKey(Buyer, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, default=None)
    quantity = models.IntegerField(default=None)
    size = models.CharField(max_length=10, default=None, null=True, blank=True)
    total = models.IntegerField(default=None)
    address1 = models.CharField(max_length=50)
    name = models.CharField(max_length=50, default=None)
    phone = models.CharField(max_length=15, default=None)
    email = models.CharField(max_length=50, default=None)
    address2 = models.CharField(max_length=50)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=20)
    notes = models.TextField(default=None)
    mode = models.CharField(max_length=20, default=None)

    def __str__(self):
        return str(self.id)

class wishlist(models.Model):
    user = models.ForeignKey(Buyer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

class Contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    msg=models.TextField()

    def __str__(self):
        return str(self.id)+" "+self.name