from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import mixins, GenericViewSet
from applications.account.models import Profile
from applications.account.permissions import IsProfileOwner

User = get_user_model()

from applications.account.serializers import ( 
        ChangePasswordSerializer, ForgotPasswordFinishSerializer, ForgotPasswordSerializer, 
        MentorSerializer, ProfileSerializer, UserSerializer
)


class UserRegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response('We have sent you an activation code to your email!')
    

class MentorRegisterApiView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = MentorSerializer
    
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response('We have sent you an activation code to your email!')



class UserActivationApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'wrong code'}, status=status.HTTP_400_BAD_REQUEST)
        


class MentorActivationApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.is_mentor = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'success'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'wrong code'}, status=status.HTTP_400_BAD_REQUEST)
        
   
    
class ChangePasswordApiView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Password chenged successfully')
    
    

class ForgotRasswordApiView(APIView):
    def post(self,request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.send_code()
        return Response('We have sent you an email')
  
    
class ForgotPasswordFinishApiview(APIView):
    def post(self, request):
        serializer = ForgotPasswordFinishSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.set_new_password()
        return Response('Your password is updated successfully')
    
    
    
class ProfileViewSet(mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwner]
    
    