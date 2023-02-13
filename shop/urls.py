from django.urls import path
from . import views

urlpatterns = [
     path('',views.index,name='index'),
     path('about',views.about,name='about'),
     path('tracking',views.tracking,name='TrackingUs'),
     path('search',views.search,name='Search'),
     path('contact',views.contact,name='ContactUS'),
     path('products/<int:myid>',views.product,name='Product'),
     path('checkout',views.checkout,name='checkout')
]
