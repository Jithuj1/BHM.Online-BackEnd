from django.urls import path, include
from .views import hospital, update


urlpatterns = [
    path('hospital', hospital, name= 'hospital'),
    path('hospital/<int:id>', update)
]
