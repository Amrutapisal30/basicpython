from django.shortcuts import render
from django.http import HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstapp.models import UserData

# Create your views here.

def Home(request):
    return HttpResponse("welcome to home page")

def About(request):
    return HttpResponse("welcome to About Page")

def Gallary(request):
    return HttpResponse("welcome to gallary page")

def Contact(request):
    return HttpResponse("welcome to contact page")

def Index(request):
    return render(request,"home.html")

def Register(request):
    return render(request,'register.html')

def Login(request):
    return render(request,"login.html")

def Bootstrapex(request):
    return render(request,"bootsex.html")

def Website(request):
    return render(request,"website.html")

def Staticex(request):
    return render(request,"staticex.html")

def Jinjaex(request):
    numbers=[45,78,89,56]
    fruites=["apple","banana","cherry","orange"]
    context={
        'name':'amruta',
        'age':29,
        'marks':numbers,
        'fruites':fruites
    }
    return render(request,"jinjaex.html",context)

@api_view(['GET'])
def sendData(request):
    return Response({'rollno':1,'name':'john'})

@api_view(['GET'])
def getAllUsers(request):
    data=UserData.objects.all().values()  #select *from userdata
    listofusers=list(data)
    return Response(listofusers)

@api_view(['GET'])
def getUser(request,username):
    userfromdb=UserData.objects.get(username=username)#select *from userdata where username="john"
    response=Response({'username':userfromdb.username,
                       'password':userfromdb.password,'mobno':userfromdb.mobno})
    return response



@api_view(['POST'])
def addUser(request):
    UserData.objects.create(
        username=request.data.get("username"),  #username="sarita"
        password=request.data.get("password"), #password="sarita123"
        mobno=request.data.get("mobno") #mobno=87655
    )
    return Response({"msg": "User added"})

@api_view(['PUT'])
def updateUser(request):
     dictionary=request.data
     userfromdb=UserData.objects.get(username=dictionary["username"])#username="anuja"
     userfromdb.password=dictionary["password"]#password='anu123'
     userfromdb.mobno=dictionary["mobno"]#mobno=45678
     userfromdb.save()
     return Response(dictionary)



@api_view(['DELETE'])
def deleteUser(request,userfromclient): 
     try:
          User=UserData.objects.filter(username=userfromclient)#username="anuja"
          if User.exists():
               User.delete()
               return Response({'message':'Record Deleted'})
          else:
               return Response({'message':'Record Not Found'}) 
     except Exception as e:
           return Response({'message':'some error occur'})

#1.update book information
#2.delete book













