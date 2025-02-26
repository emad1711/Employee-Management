from rest_framework import viewsets, permissions
from .models import Company, Department, Employee, User
from .serializers import CompanySerializer, DepartmentSerializer, EmployeeSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminOrReadOnly, IsManagerOrReadOnly
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model

# Swagger Schema View
schema_view = get_schema_view(
   openapi.Info(
      title="Employee Management API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="zaherkryem@gmail.com"),
      license=openapi.License(name="EM License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,IsAdminOrReadOnly]
    

    def get_queryset(self):
        user_id = self.request.query_params.get('id', None)
        if user_id:
            return User.objects.filter(id=user_id)
        return User.objects.all()


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]


    def get_queryset(self):
        company_id = self.request.query_params.get('id', None)
        if company_id:
            return Company.objects.filter(id=company_id)
        return Company.objects.all()

class DepartmentViewSet(viewsets.ModelViewSet):
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]


    def get_queryset(self):
        department_id = self.request.query_params.get('id', None)
        if department_id:
            return Department.objects.filter(id=department_id)
        return Department.objects.all()

class EmployeeViewSet(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsManagerOrReadOnly]

    def get_queryset(self):
        employee_id = self.request.query_params.get('id', None)
        if employee_id:
            return Employee.objects.filter(id=employee_id)
        return Employee.objects.all()







User = get_user_model()

@api_view(['POST'])
@permission_classes([AllowAny])
def custom_auth_token(request):
    email = request.data.get('email')
    username = request.data.get('username')
    password = request.data.get('password')

    if not password:
        return Response(
            {"error": "Password is required."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    user = None

    if email:
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            pass

    

    if user and user.check_password(password):
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })
    else:
        return Response(
            {"error": "Unable to log in with provided credentials."},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
@api_view(['POST'])  
@permission_classes([IsAuthenticated])  
def logout_view(request):  
    try:  
        user=request.user
        Token.objects.filter(user=user).delete() 
        
        return Response({"success": "Logout success."},status=status.HTTP_204_NO_CONTENT)  
    except (AttributeError, Token.DoesNotExist):  
        return Response({"error": "Token not found."}, status=status.HTTP_400_BAD_REQUEST)