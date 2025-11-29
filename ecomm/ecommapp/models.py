from django.db import models

# Create your models here.
class Product(models.Model): 
    product_id = models.AutoField(primary_key=True) 
    product_name = models.CharField(max_length=255) 
    quantity = models.IntegerField() 
    price = models.FloatField() 
    image_url = models.URLField(max_length=5000, null=True, blank=True)
 
    def __str__(self):   
        return f"{self.product_name} | Price: ₹{self.price} | Quantity: {self.quantity}" 
 
    class Meta: 
        db_table = "product"




#python manage.py makemigrations
#python manage.py migrate

# Create your models here.
class UserData(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    mobno=models.IntegerField()

    def __str__(self) :
        return f"""username is {self.username} and password is {self.password} 
         and mobno is {self.mobno}"""

    class Meta:
        db_table="userdata"

class OrderHistory(models.Model):
    order_id = models.AutoField(primary_key=True)
    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.FloatField()
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default="Pending")
    def __str__(self):
        return f"Order {self.order_id} - {self.customer_name} - {self.product.product_name}"
    
    class Meta:
        db_table = "order_history"

#python manage.py makemigrations
#python manage.py migrate
