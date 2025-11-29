"""
URL configuration for ecomm project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

from ecommapp.views import ProductList, add_order, add_product, addProduct, addUser, addorderhistory, deleteProduct, deleteUser, deleteordehistory, get_max_product, get_min_product, get_orders, get_product_in, get_products, get_products_gt_, get_products_lt_, getAllProducts, getAllUser, getLowStock, getProduct, getProductname, getUser, getallorder, login, register, updateOrderHistory, updatePrice, updateProduct, updateQuantity, updateUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addProduct/',addProduct),
    path('getAllProducts/',getAllProducts),
    path('getProduct/<product_id>',getProduct),
    path('get_max_product/',get_max_product),
    path('get_min_product/',get_min_product),
    path('getProductname/<product_name>',getProductname),
    path('get_product_in/<min>/<max>',get_product_in),
    path('get_products_gt_/',get_products_gt_),
    path('get_products_lt_/',get_products_lt_),
    path('updateProduct/',updateProduct),
    path('deleteProduct/<id>/',deleteProduct),
    path('getLowStock/<limit>',getLowStock),
    path('updatePrice/<product_id>',updatePrice),
    path('updateQuantity/<product_id>',updateQuantity),
      path('getAllUser/',getAllUser),
 path('getUser/<username>/',getUser),
 path('addUser/',addUser),
 path('deleteUser/<userfromclient>',deleteUser),
 path('updateUser/',updateUser),
  path('register/',register),
  path('login/',login),
  path('get_products/',get_products),
  path('add_product/',add_product),
  path('addorderhistory/',addorderhistory),
  path('getallorder/',getallorder),
  path('updateOrderHistory/',updateOrderHistory),
  path('deleteordehistory/<order_id>',deleteordehistory),
   path('products/', ProductList.as_view(), name='product-list'),
   path('get_orders/',get_orders),
   path('add_order/',add_order)
]
