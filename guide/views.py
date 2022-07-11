from django.contrib import messages
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse
from guide.models import *
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request, 'home.html')

def resorts(request):
    return render(request, 'views/resorts.html')  
def leoniaResort(request):
    return render(request, 'views/resorts/leoniaResort.html')  
def alankritaResort(request):
    return render(request, 'views/resorts/alankritaResort.html')  
def golkondaResort(request):
    return render(request, 'views/resorts/golkondaResort.html')  
def pragatiResort(request):
    return render(request, 'views/resorts/pragatiResort.html')   
def brownTownResort(request):
    return render(request, 'views/resorts/brownTownResort.html')   
def summerGreenResort(request):
    return render(request, 'views/resorts/summerGreenResort.html')     
def buttonEyesResort(request):
    return render(request, 'views/resorts/buttonEyesResort.html') 
def celebrityResort(request):
    return render(request, 'views/resorts/celebrityResort.html')     
def lahariResort(request):
    return render(request, 'views/resorts/lahariResort.html')                  

def restaurants(request):
    return render(request, 'views/restaurants.html')   
def paradise(request):
    return render(request, 'views/restaurants/paradise.html')    
def parkHyatt(request):
    return render(request, 'views/restaurants/parkHyatt.html') 
def mariott(request):
    return render(request, 'views/restaurants/mariott.html')  
def radisson(request):
    return render(request, 'views/restaurants/radisson.html')    
def novotel(request):
    return render(request, 'views/restaurants/novotel.html')         
def hyattPlace(request):
    return render(request, 'views/restaurants/hyattPlace.html') 
  

def malls(request):
    return render(request, 'views/malls.html')       
def scm(request):
    return render(request, 'views/malls/scm.html')  
def forum(request):
    return render(request, 'views/malls/forum.html')  
def inorbit(request):
    return render(request, 'views/malls/inorbit.html') 
def gvk(request):
    return render(request, 'views/malls/gvk.html')    
def nextGalleria(request):
    return render(request, 'views/malls/nextgalleria.html')   
def central(request):
    return render(request, 'views/malls/central.html')  
def cityCenter(request):
    return render(request, 'views/malls/cityCenter.html')
def manjeera(request):
    return render(request, 'views/malls/manjeera.html')
def gsm(request):
    return render(request, 'views/malls/gsm.html')                              

def historicalPlaces(request):
    return render(request, 'views/historicalPlaces.html')  
def golkondaFort(request):
    return render(request, 'views/historicalPlaces/golkondaFort.html')     
def charminar(request):
    return render(request, 'views/historicalPlaces/charminar.html')  
def qutubShahiTombs(request):
    return render(request, 'views/historicalPlaces/qutubShahiTombs.html')  
def makkahMasjid(request):
    return render(request, 'views/historicalPlaces/makkahMasjid.html')   
def chowmahallaPalace(request):
    return render(request, 'views/historicalPlaces/chowmahallaPalace.html')   
def salarJungMuseum(request):
    return render(request, 'views/historicalPlaces/salarJungMuseum.html')
def spanishMosque(request):
    return render(request, 'views/historicalPlaces/spanishMosque.html')
def toliMasjid(request):
    return render(request, 'views/historicalPlaces/toliMasjid.html')
def falaknumaPalace(request):
    return render(request, 'views/historicalPlaces/falaknumaPalace.html')                  

def amuzementParks(request):
    return render(request, 'views/amuzementParks.html')   
def wonderla(request):
    return render(request, 'views/amuzementParks/wonderla.html')  
def jalavihar(request):
    return render(request, 'views/amuzementParks/jalavihar.html')  
def wildWaters(request):
    return render(request, 'views/amuzementParks/wildWaters.html')
def escapeWater(request):
    return render(request, 'views/amuzementParks/escapeWater.html')
def mountOpera(request):
    return render(request, 'views/amuzementParks/mountOpera.html')  
def snowWorld(request):
    return render(request, 'views/amuzementParks/snowWorld.html')
def oceanPark(request):
    return render(request, 'views/amuzementParks/oceanPark.html')  
def ellesWorld(request):
    return render(request, 'views/amuzementParks/ellesWorld.html')  

def form(request):
    return render(request, 'Form/restaurant.html')    

def register(request):
    restaurant = request.POST['restaurant']
    name = request.user.first_name + ' ' + request.user.last_name
    phone = request.POST['phone']
    email = request.user.email
    date = request.POST['date']
    time = request.POST['time']
    if request.POST['attendies'] == '':
        attendies = 0
    else:
        attendies = int(request.POST['attendies'])    
    comments = request.POST['comments']
    if RegForm.objects.filter(restaurant=restaurant).exists() and RegForm.objects.filter(date=date).exists() and RegForm.objects.filter(time=time).exists():
        messages.info(request, 'This slot has been booked')
        print(messages)
        return render(request, 'Form/restaurant.html')
    else:
        slot = RegForm.objects.create(restaurant=restaurant, name=name, phone=phone, email=email, date=date, time=time, attendies=attendies, comments=comments)
        slot.save()       
        return redirect('/')