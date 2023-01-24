from django.shortcuts import render


from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import CustomUser
from .serializers import CustomUserSerializer , RegisterSerializer

# Added by Karthika V - Start Code 
from rest_framework import generics
from rest_framework.permissions import AllowAny

from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token

from users import models
# Added by Karthika V - End Code 
# Create your views here.
class CustomUserList(APIView):
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class CustomUserDetail(APIView):
    def get_object(self, pk):
        try:
            return CustomUser.objects.get(pk=pk)
        except CustomUser.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = CustomUserSerializer(user)
        return Response(serializer.data)

# Added by Karthika V - Start Code 

class RegisterUserAPIView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    print("In register API View - 1")
    permission_classes =(AllowAny, )
    print("In register API View - 2")
    

    # @api_view(['POST',])
    # def registration_view(request):
        
        
    #     if request.method == 'POST':
    #         serializer = RegisterSerializer(data=request.data)
            
    #         data ={}

    #         if serializer.is_valid():
    #             account = serializer.save()
                
    #             data['response'] = "Registration Successful!"
    #             data['username'] = account.username
    #             data['email'] =account.email

    #             token = Token.objects.get(user=account).key
    #             data['token'] = token
                
                
    #         else:
    #             data = serializer.errors
            
    #         return Response(data)

# Added by Karthika V - End  Code