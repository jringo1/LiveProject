from django.urls import include, path
from django.contrib import admin
from . import views

# URL Patterns - the first parameter is the pattern, the secd/cond is the method you're calling inside of your view
# Third is the name of the pattern/function.
urlpatterns = [
    path('', views.home, name='IntraGov'),
    path('home/', views.home, name='Home'),
    path('Politicians/', views.index, name='showPolitician'),
    path('AddToDatabase/', views.add_politician, name='addPolitician'),
    path('Politicians/<int:pk>/Details/', views.details_politician, name='politicianDetails')
    #path('polls/', include('polls.urls'))

                                 #home page
    #path('Balance of the Houses/', views.index, name='showCongress'),
                   #data scraped news from www.govtrack.us
    ]
