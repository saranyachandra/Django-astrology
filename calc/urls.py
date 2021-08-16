from django.urls import path

from . import views

urlpatterns = [
    path('genqrcode',views.genqrcode, name='genqrcode'),
    path('add',views.add, name='add'),
    path('result',views.result, name='result'),
]
