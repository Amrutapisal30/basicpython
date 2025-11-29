from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView   

from ecommapp.models import OrderHistory, Product, UserData
from ecommapp.serializers import OrderSerilizer, ProductSerilizer, UserDataSerializer
from rest_framework import status

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
import json
# Create your views here.

# POST - Add a product 
@api_view(['POST']) 
def addProduct(request): 
    
    data = request.data 
    Product.objects.create( 
        product_name=data['product_name'], 
        quantity=data['quantity'], 
        price=data['price'] ,
        image_url=data.get('image_url') 
    ) 
    return Response({'message': 'Product added successfully'}, status=201)

# GET all products 
@api_view(['GET']) 
def getAllProducts(request): 
    products = Product.objects.all()    #select *from product;
    data = [ 
        { 
            'product_id': p.product_id, 
            'product_name': p.product_name, 
            'quantity': p.quantity, 
            'price': p.price ,
            'image_url': p.image_url 
        } for p in products 
    ] 
    return Response(data) 

# GET product by ID 
@api_view(['GET']) 
def getProduct(request, product_id): 
    try: 
        product = Product.objects.get(product_id=product_id) 
        data = { 
            'product_id': product.product_id, 
            'product_name': product.product_name, 
            'quantity': product.quantity, 
            'price': product.price ,
            'image_url': product.image_url 
        } 
        return Response(data) 
    except Product.DoesNotExist: 
        return Response({'error': 'Product not found'}, status=404) 
    
@api_view(["GET"])
def get_max_product(request):
    try:
        product = Product.objects.order_by("-price").first()
        if product:
            return Response({
            'product_id': product.product_id, 
            'product_name': product.product_name, 
            'quantity': product.quantity, 
            'price': product.price ,
            'image_url': product.image_url 
            })
        else:
            return Response("Product Not Found")
    except Exception as e:
        return Response(f"Error: {str(e)}")

@api_view(["GET"])
def get_min_product(request):
    try:
        product = Product.objects.order_by("price").first()
        if product:
            return Response({
            'product_id': product.product_id, 
            'product_name': product.product_name, 
            'quantity': product.quantity, 
            'price': product.price ,
            'image_url': product.image_url 
            })
        else:
            return Response("Product Not Found")
    except Exception as e:
         return Response(f"Error: {str(e)}")
    
#To get product by product name-
@api_view(['GET'])
def getProductname(request,product_name):
    try:                              #"Laptop"           ="Laptop"
        product=Product.objects.get(product_name=product_name)  #select *from product where product_name="Tv"
        data={
            'product_id':product.product_id,
            'product_name':product.product_name,
            'quantity':product.quantity,
            'price':product.price,
            'image_url':product.image_url
        }
        return Response(data)
    except Product.DoesNotExist:
        return Response({'error':'Product Not Found'},status=404)
    
# price between 10000 to 68000
@api_view(['GET'])
def get_product_in(request,min,max):
    try:
        #select *from product where price>10000 and price<=68000
        product = Product.objects.filter(price__gte = min, price__lte = max)
        product_list = list(product.values())
        if product_list:
            return Response(product_list)
        else:
            return Response("Product not found.")
    except Exception as e:
        return Response(f"Error : {str(e)}")


# to display product whose price is greater than 50000
@api_view(['GET'])
def get_products_gt_(request):
    try:
        products = Product.objects.filter(price__gt=50000)  #SELECT * FROM product WHERE price > 50000;
        if products.exists():
            result = list(products.values())
            return Response(result)
        else:
            return Response({"message": "No products found with price greater than 50000."})
    except Exception as e:
        return Response({"error": str(e)})
# to display product whose price is less than 50000
@api_view(['GET'])
def get_products_lt_(request):
    try:
        products = Product.objects.filter(price__lt=50000)  #SELECT * FROM product WHERE price < 50000;
        if products.exists():
            result = list(products.values())
            return Response(result)
        else:
            return Response({"message": "No products found with price greater than 50000."})
    except Exception as e:
        return Response({"error": str(e)})

# PUT - Update a product 
@api_view(['PUT']) 
def updateProduct(request): 
    data = request.data 
    try: 
        product = Product.objects.get(product_id=data['product_id']) 
        product.product_name = data['product_name'] 
        product.quantity = data['quantity'] 
        product.price = data['price'] 
        product.image_url = data.get('image_url', product.image_url) 
        product.save() 
        return Response({'message': 'Product updated successfully'}) 
    except Product.DoesNotExist: 
        return Response({'error': 'Product not found'}, status=404) 
    
# DELETE - Delete a product 
@api_view(['DELETE']) 
def deleteProduct(request, id): 
    try: 
        product = Product.objects.get(product_id=id) 
        product.delete() 
        return Response({'message': 'Product deleted successfully'}) 
    except Product.DoesNotExist: 
        return Response({'error': 'Product not found'}, status=404)
#path('deleteProduct/<id>/',deleteProduct),

# 1. Update Product
# 2. Delete Product
# 3. Get Low Stock Products (quantity < 10)
# get low stock product
@api_view(['GET'])
def getLowStock(request, limit):
    try:
        products = Product.objects.filter(quantity__lte=limit)
        if products.exists():
            return Response(list(products.values()))
        else:
            return Response({"message": f"No products found with quantity ≤ {limit}."})
    except Exception as e:
        return Response({"error": str(e)})
# 4. Update Only Price of a Product
# Update only price of the product 
@api_view(['PATCH'])
def updatePrice(request, product_id):
    try:
        new_price = request.data.get('price')
        if new_price is None:
            return Response({"error": "Price is required"}, status=400)
        product = Product.objects.get(product_id=product_id)
        product.price = new_price
        product.save()
        return Response({"message": "Price updated successfully!"})
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)
# 5. Update Only Quantity of a Product
# update only Quantity of a product
@api_view(['PATCH'])
def updateQuantity(request,product_id):
    try:
        new_qua=request.data.get('quantity')
        if new_qua is None:
            return Response({"error": "Quantity is required"}, status=400)
        product = Product.objects.get(product_id=product_id)
        product.quantity = new_qua
        product.save()
        return Response({"message": "Quantity updated successfully!"})
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=404)

# 6. Get Max Quantity Product
# 7. Get Min Quantity Product

#userdata-
# 1)getAlluser
# 2)getUser-id
# 3)addUser
# 4)deleteUser
# 5)UpdateUser
@api_view(['GET'])
def getAllUser(request):
    queryset= UserData.objects.all().values()  #select *from Userdata
    listofusers=list(queryset)
    return Response(listofusers)

@api_view(['GET'])
def getUser(request,username):
     userfromdb=UserData.objects.get(username=username)#select *from User where username="admin"
     response=Response({'username':userfromdb.username,
                        'password':userfromdb.password,'mobno':userfromdb.mobno})
     return response


@api_view(['POST'])
def addUser(request):
     print(request.data)
     userfromclient=request.data
     UserData.objects.create(username=userfromclient['username'],
                             password=userfromclient['password'],
                             mobno=userfromclient['mobno'])
     #insert into userdata values('kartik','kartik123',789677)
     response=Response(userfromclient)
     return(response)

@api_view(['DELETE'])
def deleteUser(request,userfromclient):
     
     try:
          User=UserData.objects.filter(username=userfromclient)
          if User.exists():
               User.delete()
               return Response({'message':'Record Deleted'})
          else:
               return Response({'message':'Record Not Found'}) 
     except Exception as e:
           return Response({'message':'some error occur'})
 
     #return Response({'message':'Record Deleted'})

@api_view(['PUT'])
def updateUser(request):
     dictionary=request.data
     userfromdb=UserData.objects.get(username=dictionary["username"])#select *from userdata where username='pooja'
     userfromdb.password=dictionary["password"]
     userfromdb.mobno=dictionary["mobno"]
     userfromdb.save()
     return Response(dictionary)


@api_view(['POST'])
def register(request):
    if UserData.objects.filter(username=request.data.get('username')).exists():
        return Response({'error': 'Username already taken'},
                         status=status.HTTP_400_BAD_REQUEST)

    serializer = UserDataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully'}, 
                        status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#user login
#admin login


@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        # 1) First check if admin (Django default admin)
        admin_user = authenticate(username=username, password=password)
        if admin_user is not None:
            if admin_user.is_staff or admin_user.is_superuser:
                return JsonResponse({
                    "message": "Login successful",
                    "role": "admin",
                    "username": admin_user.username
                }, status=200)
 # 2) If not admin â†’ check in UserData table
        try:
            user = UserData.objects.get(username=username, password=password)
            return JsonResponse({
                "message": "Login successful",
                "role": "user",
                "username": user.username,  
            }, status=200)
        except UserData.DoesNotExist:
            return JsonResponse({"error": "Invalid username or password"}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)

#Serilizer and deserilizer in DRF
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()  #select *from product
    serializer = ProductSerilizer(products, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_product(request):
    serializer = ProductSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Product added successfully"})
    return Response(serializer.errors)


#1)getOrder
#2)addOrder

# Using Serializer 
# 1. get Order 
@api_view(['GET'])
def get_orders(request):
    orders = OrderHistory.objects.all()               
    serializer = OrderSerilizer(orders, many=True)
    return Response(serializer.data)

# 2. addOrder
@api_view(['POST'])
def add_order(request):
    serializer = OrderSerilizer(data=request.data)
    if serializer.is_valid():
        serializer.save()                 
        return Response({"msg": "Order placed successfully"})
    return Response(serializer.errors)

@api_view(['POST'])
def addorderhistory(request):
    data = request.data
    print(data)
    try:
        # Get product using product_id from client request
        product_obj = Product.objects.get(product_id=data['product_id'])
        # Create order history record
        order = OrderHistory.objects.create(
            customer_name=data['customer_name'],
            customer_email=data['customer_email'],
            product=product_obj,        # FOREIGN KEY
            quantity=data['quantity'],
            total_price=data['total_price'],
            status=data['status']
            # order_date auto_now_add=True (no need to send)
        )
        return Response({
            "message": "Order created successfully",
            "order_id": order.order_id
        }, status=201)
    except Product.DoesNotExist:
        return Response({"error": "Invalid product_id"}, status=400)
    except Exception as e:
        return Response({"error": str(e)}, status=500)


#order table
@api_view(['GET'])
def getallorder(request):
    orders = OrderHistory.objects.all()
    data = [
        {
            'order_id': p.order_id,
            'customer_name': p.customer_name,
            'customer_email': p.customer_email,
            'product': p.product.product_name,
            'quantity': p.quantity,
            'total_price': p.total_price,
            'order_date': p.order_date,
            'status': p.status,
        }
        for p in orders
    ]
    return Response(data)

# #update order history
# @api_view(['PUT'])
# def updateorderhistory(request, order_id):
#     data=request.data
#     try:
#         order=OrderHistory.objects.get(order_id=order_id)
#         order.status=data.get('status', order.status)
#         order.save()
#         return Response({"message": "Order status updated successfully"})
#     except OrderHistory.DoesNotExist:
#         return Response({"error": "Order not found"}, status=404)

# update order history 
@api_view(['PUT'])
def updateOrderHistory(request):
    data = request.data
    try:
        order = OrderHistory.objects.get(order_id=data['order_id'])
        # Update fields
        order.customer_name = data.get('customer_name', order.customer_name)
        order.customer_email = data.get('customer_email', order.customer_email)
        # Update product if provided
        if 'product_id' in data:
            try:
                product_obj = Product.objects.get(product_id=data['product_id'])
                order.product = product_obj
            except Product.DoesNotExist:
                return Response({'Error': 'Invalid Product_id'}, status=400)
        order.quantity = data.get('quantity', order.quantity)
        order.total_price = data.get('total_price', order.total_price)
        order.status = data.get('status', order.status)
        order.save()
        return Response({'message': 'Order updated successfully'})
    except OrderHistory.DoesNotExist:
        return Response({'Error': 'Order Not Found'}, status=404)


#delete order history
@api_view(['DELETE'])
def deleteordehistory(request, order_id):
    try:
        order=OrderHistory.objects.get(order_id=order_id)
        order.delete()
        return Response({"message":"Order deleted successfully"})
    except OrderHistory.DoesNotExist:
        return Response({"error":"Order not found"}, status=404)


class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerilizer(products, many=True)
        return Response(serializer.data)    






