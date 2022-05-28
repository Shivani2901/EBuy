"""EBuy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('verify/<str:token>/', views.verify),
    path('sign/', views.sign),
    path('cart/',views.cartDetails),
    path('checkout/',views.checkoutDetails),
    path('contact/',views.contactDetails),
    path('about/',views.about),
    path('shop/<str:cat>/',views.shopDetails),
    path('product/<int:num>/', views.productDetails),
    path('wishlist/<int:num>/', views.wishlistDetails),
    path('wishlist/', views.wishlistBuyer),
    path('deletewishlist/<int:num>/', views.wishlistDelete),
    path('login/',views.loginDetails),
    path('logout/', views.logout),
    path('account/',views.myAccount),
    path('register/', views.registerDetails),
    path('profile/', views.profile),
    path('addproduct/', views.addProduct),
    path('deleteproduct/<int:num>/', views.deleteProduct),
    path('editproduct/<int:num>/', views.editProduct),
    path('deletecart/<int:num>/', views.deletecart),
    path('confirm/', views.confirm),
    path('note/', views.note),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
