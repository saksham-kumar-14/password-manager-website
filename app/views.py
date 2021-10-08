from django.http.response import HttpResponse
from django.shortcuts import redirect, render,HttpResponse,redirect 
import pymongo 
import random 
from string import printable

MASTER_KEY = "saksham"
CLIENT = pymongo.MongoClient("mongodb://localhost:27017/")
DB = CLIENT["password_manager"]
COLLECTION = DB['password_with_website'] 

# Create your views here.
def home(request):

    return render(request,"home.html") 


def create(request):
    global MASTER_KEY,CLIENT,DB,COLLECTION

    if request.method == "POST" :
        data = request.POST.dict()
        entered_key = data.get("entered-key") 
        if entered_key == MASTER_KEY:
            website_name = data.get("website-name")
            password = data.get("password")
            email_address = data.get("email") 

            if len(email_address) < 6:
                return render(request,"result.html",{"advice": "Please provide a valid email address"}) 

            #doing pymongo creating work
            insert_value = {"website" : website_name,"email" : email_address,"password" : password}
            COLLECTION.insert_one(insert_value) 

            return render(request,"result.html",{"advice" : "Password saved"})
        else:
            return render(request,"result.html",{"advice" : "Provided key is not the master key"})

    return render(request,"create.html")


def read(request):
    global MASTER_KEY,CLIENT,DB,COLLECTION

    if request.method == 'POST':
        data = request.POST.dict()
        entered_key = data.get("entered-key")
        if entered_key == MASTER_KEY:
            website_name = data.get("website-name")
            
            if website_name == "":
                context = {"advice" : "Please enter a valid website name"}
                return(request,"result.html",context)
            #reading the mongo db
            find_value = {"website" : website_name}
            result = COLLECTION.find_one(find_value)
            if(result == None):
                context = {"advice" : "This website is not present in our database"}
            else: 
                context = {"email" : f"e - mail : {result['email']}" , "password" : f"Password : {result['password']}" }
            return render(request,'result.html',context)   
            
        else:
            return render(request,"result.html",{"advice" : "The key provided is not the master key"})

    return render(request,"read.html") 
