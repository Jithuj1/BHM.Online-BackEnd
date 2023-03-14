from django.urls import path, include
from .views import doctor, departments, update, dept, schedule


urlpatterns = [
    path('doctor', doctor),
    path('doctor/<int:id>', update),
    path('department', departments),
    path('department/<int:id>', dept),
    path('schedule', schedule),
]
