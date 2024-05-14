from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, status
from .serializer import MainUserSerializer, MyTokenObtainPairSerializer
from .models import MainUser
from .permissions import AnnonPermission


class LoginView(TokenObtainPairView):
    permission_classes = (AnnonPermission,)
    serializer_class = MyTokenObtainPairSerializer


class UserRegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = MainUserSerializer(data=request.data)
        if serializer.is_valid():
            seller = MainUser.objects.create(
                email=request.data['email'],
                is_Seller=True,
            )
            seller.set_password(request.data['password'])
            seller.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
