from django.urls import path, include
from .views import RoomsData, singleMessages, Notifications, getRoom, updateNotification, getMessage, UpdateRoom


urlpatterns = [
    path('rooms', RoomsData),
    path('messages', singleMessages),
    path('notification', Notifications),
    path('get_room/<int:patient>/<int:doctor>', getRoom),
    path('updateNotification/<int:id>', updateNotification),
    path('get_message/<int:id>', getMessage),
    path('update_room/<int:id>', UpdateRoom),
]

