from django.urls import path

from . import views

urlpatterns = [
    path('',views.index, name='index'),   
    path('astro_details/<int:id>/',views.astro_details, name='astro_details'),
    path('search',views.search, name='search'),
    
]
