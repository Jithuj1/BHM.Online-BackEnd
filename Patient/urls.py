from django.urls import path, include
from .views import MyTokenObtainPairView, patient, update
from . import views
from rest_framework_simplejwt import views as jwt_views


from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('patient', patient, name= 'patient'),
    path('patient/<int:id>', update),
    path('appointments', views.AppointmentListView.as_view()),
    path('appointments/<int:id>', views.AppointmentListDetail.as_view()),
]
