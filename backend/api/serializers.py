from rest_framework import serializers
from .models import Company, Department, Employee, User

class UserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = User  
        fields = ['id', 'username', 'email', 'password', 'role']  
        extra_kwargs = {  
            'password': {'required': False, 'write_only': True}  
        }  
    def create(self, validated_data):
       
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            role=validated_data['role'],
        )

        return user
    
    def update(self, instance, validated_data):  
        password = validated_data.pop('password', None)  
        if password is not None:  
            instance.set_password(password)  
        
        return super().update(instance, validated_data) 


class CompanySerializer(serializers.ModelSerializer):
    department_count = serializers.ReadOnlyField()
    employee_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Company
        fields = ['id', 'name', 'department_count', 'employee_count']

class DepartmentSerializer(serializers.ModelSerializer):
    employee_count = serializers.ReadOnlyField()
    
    class Meta:
        model = Department
        fields = ['id', 'company', 'name', 'employee_count']

class EmployeeSerializer(serializers.ModelSerializer):
    work_days = serializers.ReadOnlyField()
    
    class Meta:
        model = Employee
        fields = ['id', 'company', 'department', 'status', 'name', 'email', 'phone_number', 'address', 'job_title', 'hire_date', 'work_days']
