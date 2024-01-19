
from django.urls import path
from . import views


urlpatterns = [

    # Add task 
    path('', views.index, name='index'),
    path('start/<int:pk>',views.start_date, name='start_date'),
    path('end/<int:pk>',views.end_date, name='end_date'),
]