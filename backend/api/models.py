from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.core.validators import RegexValidator
from datetime import date

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        extra_fields.setdefault('username', None) 
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
# User model with role field
class User(AbstractUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, blank=True, null=True) 
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email



# Company model
class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    
    def department_count(self):
        return self.departments.count()
    
    def employee_count(self):
        return Employee.objects.filter(company=self).count()
    
    def __str__(self):
        return self.name

# Department model
class Department(models.Model):
    company = models.ForeignKey(Company, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    
    def employee_count(self):
        return Employee.objects.filter(department=self).count()
    
    def __str__(self):
        return f"{self.name} ({self.company.name})"

# Employee model
class Employee(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )
    
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^[0-9]{10,15}$', message="Phone number must be between 10 and 15 digits.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    address = models.TextField()
    job_title = models.CharField(max_length=255)
    hire_date = models.DateField(null=True, blank=True)
    
    @property
    def work_days(self):
        if self.hire_date and self.status =='active':
            return (date.today() - self.hire_date).days
        return None
    
    def clean(self):
        if self.department.company != self.company:
            raise ValueError("Department must belong to the selected company.")
    
    def __str__(self):
        return f"{self.name} - {self.job_title} ({self.company.name})"
