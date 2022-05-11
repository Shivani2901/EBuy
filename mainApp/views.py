from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
    if (request.method == "POST"):
        msg = request.POST.get('message')
        p = Product.objects.filter(Q(name__icontains=msg))
    else:
        p = Product.objects.all()
    return render(request, "index.html", {"Product": p})

@login_required(login_url='/login/')
def cartDetails(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    try:
        Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        b = Buyer.objects.get(uname=request.user)
        cart = Cart.objects.filter(buyer=b)
        subtotal = 0
        for i in cart:
            subtotal += i.total
        if (subtotal < 1000):
            delievery = 150
        else:
            delievery = 0
        finalAmount = subtotal + delievery
        return render(request, "cart.html",
                      {"Cart": cart, "Sub": subtotal, "Delievery": delievery, "Final": finalAmount})


@login_required(login_url='/login/')
def deletecart(request,num):
    cart = Cart.objects.get(id=num)
    cart.delete()
    return HttpResponseRedirect('/cart/')

@login_required(login_url='/login/')
def checkoutDetails(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        c = Cart.objects.filter(buyer=user)
        subtotal = 0
        for i in c:
            subtotal += i.total
        if (subtotal < 1000):
            delievery = 150
        else:
            delievery = 0
        finalAmount = subtotal + delievery
        if (request.method == "POST"):
            ch = Checkout()
            ch.user = user
            ch.address1 = request.POST.get('address1')
            ch.address2 = request.POST.get('address2')
            ch.city = request.POST.get('city')
            ch.state = request.POST.get('state')
            ch.pin = request.POST.get('pin')
            ch.name = request.POST.get('name')
            ch.email = request.POST.get('email')
            ch.phone = request.POST.get('phone')
            cart = Cart.objects.filter(buyer=user)
            ch.cart = cart[0]
            ch.total = cart[0].total
            ch.mode = request.POST.get('option')
            ch.notes = request.POST.get('message')
            ch.save()

            return HttpResponseRedirect('/confirm/')
        return render(request, "checkout.html", {
            "user": user, "cart": c ,"Sub": subtotal, "Delievery": delievery, "Final": finalAmount})

def confirm(request):
    return render(request, "confirm.html")

def contactDetails(request):
    if(request.method=="POST"):
        c=Contact()
        c.name=request.POST.get('name')
        c.email=request.POST.get('email')
        c.subject=request.POST.get('subject')
        c.msg=request.POST.get('message')
        c.save()
        messages.success(request,"Message Sent")
        return HttpResponseRedirect('/contact/')
    return render(request,"contact-us.html")

def about(request):
    return render(request,"about.html")

@login_required(login_url='/login/')
def wishlistDetails(request, num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        w = wishlist()
        product = Product.objects.get(id=num)
        w.user = user
        w.product = product
        w.save()
        return HttpResponseRedirect('/wishlist/')

@login_required(login_url='/login/')
def wishlistBuyer(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin')
    try:
        user = Seller.objects.get(uname=request.user)
        return HttpResponseRedirect('/profile/')
    except:
        user = Buyer.objects.get(uname=request.user)
        wish = wishlist.objects.filter(user=user)
        return render(request,"wishlist.html",
                                 {"Wish": wish})

@login_required(login_url='/login/')
def wishlistDelete(request, num):
    wish = wishlist.objects.get(id=num)
    wish.delete()
    return HttpResponseRedirect('/wishlist/')

def loginDetails(request):
    if(request.method=="POST"):
        uname = request.POST.get('uname')
        pward = request.POST.get('password')
        user = auth.authenticate(username=uname, password=pward)
        if(user is not None):
            auth.login(request, user)
            return HttpResponseRedirect('/profile/')
        else:
            messages.error(request, "Invalid User Name or Password")
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/account/')

def productDetails(request,num):
    p = Product.objects.get(id=num)
    if(request.method=="POST"):
        try:
            c = Cart()
            b = Buyer.objects.get(uname=request.user)
            c.product = p
            c.buyer = b
            c.quantity = int(request.POST.get('q'))
            c.total = c.product.finalPrice * c.quantity
            c.save()
            return HttpResponseRedirect('/cart/')
        except:
            return HttpResponseRedirect('/login/')
    return render(request, "product-detail.html", {"Product": p})

def shopDetails(request,cat):
    c = Category.objects.all()
    brand = Brand.objects.all()
    if (cat == "default" ):
        p = Product.objects.all()
    else:
        cobj = Category.objects.get(name=cat)
        p = Product.objects.filter(category=cobj)
    return render(request, "shop.html", {"Category": c, "Brand": brand, "Product": p, "Cat": cat,
                                         })

def myAccount(request):
    return render(request,"my-account.html")

def signUp(request):
    return render(request,"register.html")

def registerDetails(request):
    choice = request.POST.get('option')
    if(choice=="seller"):
        s = Seller()
        s.name = request.POST.get('name')
        s.uname = request.POST.get('username')
        s.email = request.POST.get('email')
        pward = request.POST.get('password')
        try:
            user= User.objects.create_user(username=s.uname,
                                       email=s.email,
                                       password=pward)
            # user = User.objects.create_user(s.name,
            #                              s.email,
            #                              pward)
            # user = User.objects.create_user('abc',
            #                                 'abc@gmail.com',
            #                                 'abracadabre')
            s.save()
            messages.success(request, "Account created please Login!!")
            return HttpResponseRedirect('/login/')
        except:
            messages.error(request, "User Already Exist")
            return render(request,"register.html")
    else:
        b=Buyer()
        b.name = request.POST.get('name')
        b.uname = request.POST.get('username')
        b.email = request.POST.get('email')
        pward = request.POST.get('password')
        try:
            user = User.objects.create_user(username=b.uname,email=b.email,password=pward)
            b.save()
            messages.success(request, "Account created please Login!!")
            return HttpResponseRedirect('/login/')
        except:
            messages.error(request, "User Already Exist")
            return render(request,"register.html")


@login_required(login_url='/login/')
def profile(request):
    user = User.objects.get(username=request.user)
    if(user.is_superuser):
         return HttpResponseRedirect('/admin/')
    else:
        try:
             s=Seller.objects.get(uname=request.user)
             products=Product.objects.filter(seller=s)
             if(request.method=="POST"):
                 s.name = request.POST.get('name')
                 s.email = request.POST.get('email')
                 s.phone = request.POST.get('phone')
                 s.bankName = request.POST.get('bank')
                 s.ifscCode = request.POST.get('ifsc')
                 s.accountNumber = request.POST.get('account')
                 s.save()
                 return HttpResponseRedirect('/profile/')
             #return render(request, "seller.html")
             #return render(request, "index.html")
             return render(request,"seller.html", {"User": s, "Product": products})
        except:
            b = Buyer.objects.get(uname=request.user)
            if (request.method == "POST"):
                b.name = request.POST.get('name')
                b.email = request.POST.get('email')
                b.phone = request.POST.get('phone')
                b.address1 = request.POST.get('address1')
                b.address2 = request.POST.get('address2')
                b.city = request.POST.get('city')
                b.state = request.POST.get('state')
                b.pin = request.POST.get('pin')
                b.save()
                return HttpResponseRedirect('/profile/')
            return render(request, "buyer.html", {"User": b})

@login_required(login_url='/login/')
def addProduct(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    brand = Brand.objects.all()
    category = Category.objects.all()
    # sub = SubCategory.objects.all()
    if(request.method=="POST"):
        try:
            s = Seller.objects.get(uname=request.user)
            p=Product()
            p.name=request.POST.get('name')
            p.desc=request.POST.get('description')
            p.basePrice=int(request.POST.get('baseprice'))
            p.discount=int(request.POST.get('discount'))
            p.finalPrice = p.basePrice - (p.basePrice * (p.discount * 0.01))
            p.category=Category.objects.get(name=request.POST.get('category'))
            p.brand=Brand.objects.get(name=request.POST.get('brand'))
            # p.subcategory=SubCategory.objects.get(name=request.POST.get('subcategory'))
            p.img1 = request.FILES.get('img1')
            p.img2 = request.FILES.get('img2')
            p.img3 = request.FILES.get('img3')
            p.img4 = request.FILES.get('img4')
            p.seller = s
            p.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request,"addproduct.html", {"Brand": brand,"Category": category,})


@login_required(login_url='/login/')
def deleteProduct(request,num):
    user=User.objects.get(username=request.user)
    if(user.is_superuser):
        return HttpResponseRedirect('/admin/')
    p=Product.objects.get(id=num)
    p.delete()
    return HttpResponseRedirect('/profile/')

@login_required(login_url='/login/')
def editProduct(request,num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    p = Product.objects.get(id=num)
    category=Category.objects.all()
    brand=Brand.objects.all()
    if(request.method =="POST"):
        s = Seller.objects.get(uname=request.user)
        p.name = request.POST.get('name')
        if(not request.POST.get('description')==''):
            p.desc = request.POST.get('description')
        p.basePrice = int(request.POST.get('baseprice'))
        p.discount = int(request.POST.get('discount'))
        p.finalPrice = p.basePrice - (p.basePrice * (p.discount * 0.01))
        p.category = Category.objects.get(name=request.POST.get('category'))
        p.brand = Brand.objects.get(name=request.POST.get('brand'))
        if(not request.FILES.get('img1')==None):
            p.img1 = request.FILES.get('img1')
        if (not request.FILES.get('img2') == None):
         p.img2 = request.FILES.get('img2')
        if (not request.FILES.get('img3') == None):
            p.img3 = request.FILES.get('img3')
        if (not request.FILES.get('img4') == None):
            p.img4 = request.FILES.get('img4')
        p.seller = s
        p.save()
        return HttpResponseRedirect('/profile/')
    return render(request, "editproduct.html", {
                                                "Product": p,
                                                 "Category":category,
                                                  "Brand":brand})
