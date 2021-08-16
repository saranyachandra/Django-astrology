from django.urls import path
from . import views

urlpatterns = [
    path('show_details', views.show_details, name='show_details'),
    path('pdf_report_create', views.pdf_report_create, name='pdf_report_create'),
]
