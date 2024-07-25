from django.urls import path
from .views import RoomsList, GameDetailView

urlpatterns = [
    path('rooms/', RoomsList.as_view(), name='rooms-list'),
    path('games/<int:room_id>/', GameDetailView.as_view(), name='game-detail'),

]