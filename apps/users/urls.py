from django.urls import path
from .views import LoginView, UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='user-registration'),
    path('login/', LoginView.as_view(), name='user-login')
]