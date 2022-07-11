from django.urls import path
from . import views 

urlpatterns = [
    path('',views.home, name='home'),
    path('home.html', views.home),

    path('views/resorts.html', views.resorts),
    path('views/resorts/leoniaResort.html', views.leoniaResort),
    path('views/resorts/alankritaResort.html', views.alankritaResort),
    path('views/resorts/golkondaResort.html', views.golkondaResort),
    path('views/resorts/pragatiResort.html', views.pragatiResort),
    path('views/resorts/brownTownResort.html', views.brownTownResort),
    path('views/resorts/summerGreenResort.html', views.summerGreenResort),
    path('views/resorts/buttonEyesResort.html', views.buttonEyesResort),
    path('views/resorts/celebrityResort.html', views.celebrityResort),
    path('views/resorts/lahariResort.html', views.lahariResort),

    path('views/restaurants.html', views.restaurants),
    path('views/restaurants/paradise.html', views.paradise),
    path('views/restaurants/parkHyatt.html', views.parkHyatt),
    path('views/restaurants/mariott.html', views.mariott),
    path('views/restaurants/radisson.html', views.radisson),
    path('views/restaurants/novotel.html', views.novotel),
    path('views/restaurants/hyattPlace.html', views.hyattPlace),

    path('views/restaurants/Form/restaurant.html', views.form),
    path('views/restaurants/Form/register', views.register, name="register"),

    path('views/malls.html', views.malls),
    path('views/malls/scm.html', views.scm),
    path('views/malls/forum.html', views.forum),
    path('views/malls/inorbit.html', views.inorbit),
    path('views/malls/gvk.html', views.gvk),
    path('views/malls/nextGalleria.html', views.nextGalleria),
    path('views/malls/central.html', views.central),
    path('views/malls/cityCenter.html', views.cityCenter),
    path('views/malls/manjeera.html', views.manjeera),
    path('views/malls/gsm.html', views.gsm),

    path('views/historicalPlaces.html', views.historicalPlaces),
    path('views/historicalPlaces/golkondaFort.html', views.golkondaFort),
    path('views/historicalPlaces/charminar.html', views.charminar),
    path('views/historicalPlaces/qutubShahiTombs.html', views.qutubShahiTombs),
    path('views/historicalPlaces/makkahMasjid.html', views.makkahMasjid),
    path('views/historicalPlaces/chowmahallaPalace.html', views.chowmahallaPalace),
    path('views/historicalPlaces/salarJungMuseum.html', views.salarJungMuseum),
    path('views/historicalPlaces/spanishMosque.html', views.spanishMosque),
    path('views/historicalPlaces/toliMasjid.html', views.toliMasjid),
    path('views/historicalPlaces/falaknumaPalace.html', views.falaknumaPalace),

    path('views/amuzementParks.html', views.amuzementParks),
    path('views/amuzementParks/wonderla.html', views.wonderla),
    path('views/amuzementParks/jalavihar.html', views.jalavihar),
    path('views/amuzementParks/wildWaters.html', views.wildWaters),
    path('views/amuzementParks/escapeWater.html', views.escapeWater),
    path('views/amuzementParks/mountOpera.html', views.mountOpera),
    path('views/amuzementParks/snowWorld.html', views.snowWorld),
    path('views/amuzementParks/oceanPark.html', views.oceanPark),
    path('views/amuzementParks/ellesWorld.html', views.ellesWorld),

]