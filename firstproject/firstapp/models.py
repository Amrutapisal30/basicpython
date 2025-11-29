from django import forms
from django.db import models
# Create your models here.
# Model class is a class which inherites from models.Model class .
# It represent database table having same name
# Model represent data of application . It is M from MVT(Model View Template)

class UserData(models.Model):
    username=models.CharField(max_length=20,primary_key=True)
    password=models.CharField(max_length=20)
    mobno=models.IntegerField()

    def __str__(self) :
        return f"username is {self.username} and password is {self.password} and mobno is {self.mobno}"
    
    class Meta:
        db_table="userdata"

#create table userdata(username varchar(20),password varchar(20),mobno int);



class Book(models.Model):
    bookid=models.IntegerField()
    name=models.CharField(max_length=20)
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self) :
        return f"bookid is {self.bookid} and name is {self.name} and   quantity:{self.quantity} and price is {self.price}"
    
    class Meta:
        db_table="book"













