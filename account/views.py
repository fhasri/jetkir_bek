from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters 
from rest_framework.generics import ListAPIView , CreateAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import RegisterSerializer, GetUserSerializers , RegisterCourierSerializer
from .models import User
from drf_yasg.utils import swagger_auto_schema






class RegisterView(APIView):
    @swagger_auto_schema(request_body=RegisterSerializer())
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully registered', status=201)


class ActivationView(APIView):

    def get(self, request, email, activation_code):
        user = User.objects.filter(email=email, activation_code=activation_code).first()
        if not user:
            return Response('User does not exist', status=400)
        user.activation_code = ''
        user.is_active = True
        user.save()
        return Response('Activated', status=200)

class RegisterCourierView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterCourierSerializer
    permission_classes= [IsAuthenticated]


# class RegisterCourierView(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         email = request.data.get('email')
#         surname = request.data.get('surname')
#         passport_image = request.data.get('passport_image')
#         techpassport_image = request.data.get('techpassport_image')
#         transport_image = request.data.get('transport_image')

#         user = User.objects.filter(email=email).first()
#         if user:
#             user.surname = surname
#             user.passport_image = passport_image
#             user.techpassport_image = techpassport_image
#             user.transport_image = transport_image
#             user.save()
#             return Response('Registered! Wait for response', status=200)
#         else:
#             return Response('User not found', status=404)
        

class ActivateCourierView(APIView):
    def post(self, request):
        email = request.data.get('email')
        user = User.objects.get(email=email)
        if user:
            user.is_curier = True
            user.save()
            return Response('Activated', status=200)
        else:
            return Response('User not found', status=404)
    permission_classes = [IsAdminUser]


class GetUserView(ListAPIView):
        queryset = User.objects.all()
        serializer_class = GetUserSerializers





