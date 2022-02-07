"""merchex URL Configuration

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
from django.urls import path
from listings import views

# Les chemins URL
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/', views.band_list, name='band-list'), # Voir la liste
    path('bands/<int:id>/', views.band_detail, name='band-detail'), # Pour voir chaque élément via l'id
    path('bands/add', views.band_create, name='band-create'), # Pour créer un formumaire : band
    path('about-us/', views.about),
    path('listings/', views.listing_list, name='listing-list'),
    path('listings/<int:id>', views.listing_detail, name='listing-detail'),
    path('contact-us/', views.contact, name='contact'),
    #path('listings/', views.email_sent, name='email-sent')
]

