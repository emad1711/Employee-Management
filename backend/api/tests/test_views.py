from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model
from api.models import Company, Department, Employee
from rest_framework.authtoken.models import Token

User = get_user_model()



class BaseAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="user1@example.com",
            password="pass123",
            role="employee"
        )

        self.manager_user = User.objects.create_user(
            email="manager@example.com",
            password="manager123",
            role="manager"
        )

        self.admin_user = User.objects.create_superuser(
            email="admin@example.com",
            password="admin123",
            role="admin"
        )

        self.company = Company.objects.create(name="Test Company")
        self.department = Department.objects.create(name="HR", company=self.company)
        self.employee = Employee.objects.create(
            company=self.company,
            department=self.department,
            status="active",
            name="John Doe",
            email="johndoe@example.com",
            phone_number="1234567890",
            address="Test Address",
            job_title="Developer"
        )

        self.user_token, _ = Token.objects.get_or_create(user=self.user)
        self.manager_token, _ = Token.objects.get_or_create(user=self.manager_user)
        self.admin_token, _ = Token.objects.get_or_create(user=self.admin_user)

        self.company_url = "/api/companies/"
        self.department_url = "/api/departments/"
        self.employee_url = "/api/employees/"
        self.user_url = "/api/users/"


class UserViewSetTest(BaseAPITestCase):
    def test_get_users_unauthenticated(self):
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_users_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        response = self.client.get(self.user_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CompanyViewSetTest(BaseAPITestCase):
    def test_get_companies_unauthenticated(self):
        response = self.client.get(self.company_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_companies_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        response = self.client.get(self.company_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_company_as_admin(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.admin_token.key}')
        data = {"name": "New Company"}
        response = self.client.post(self.company_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DepartmentViewSetTest(BaseAPITestCase):
    def test_get_departments_unauthenticated(self):
        response = self.client.get(self.department_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_departments_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        response = self.client.get(self.department_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_department_as_manager(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.manager_token.key}')
        data = {"name": "Finance", "company": self.company.id}
        response = self.client.post(self.department_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class EmployeeViewSetTest(BaseAPITestCase):
    def test_get_employees_unauthenticated(self):
        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_employees_authenticated(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.user_token.key}')
        response = self.client.get(self.employee_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_employee_as_manager(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.manager_token.key}')
        data = {
            "company": self.company.id,
            "department": self.department.id,
            "status": "active",
            "name": "New Employee",
            "email": "newemployee@example.com",
            "phone_number": "0987654321",
            "address": "New Address",
            "job_title": "Designer"
        }
        response = self.client.post(self.employee_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
