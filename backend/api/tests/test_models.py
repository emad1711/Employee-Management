from django.test import TestCase
from django.contrib.auth import get_user_model
from api.models import Company, Department, Employee
from datetime import date
User = get_user_model()





# Unit Tests
class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(email='test@example.com', password='password123', role='employee')
        self.assertEqual(user.email, 'test@example.com')
        self.assertEqual(user.role, 'employee')
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        superuser = User.objects.create_superuser(email='admin@example.com', password='admin123')
        self.assertEqual(superuser.email, 'admin@example.com')
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)


class CompanyModelTest(TestCase):
    def test_create_company(self):
        company = Company.objects.create(name='Test Company')
        self.assertEqual(company.name, 'Test Company')
        self.assertEqual(company.department_count(), 0)
        self.assertEqual(company.employee_count(), 0)

    def test_department_count(self):
        company = Company.objects.create(name='Test Company')
        Department.objects.create(company=company, name='Admin')
        Department.objects.create(company=company, name='IT')
        self.assertEqual(company.department_count(), 2)

    def test_employee_count(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        Employee.objects.create(company=company, department=department, name='John Doe', email='john@example.com', phone_number='1234567890', address='123 Street', job_title='HR Manager')
        self.assertEqual(company.employee_count(), 1)


class DepartmentModelTest(TestCase):
    def test_create_department(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        self.assertEqual(department.name, 'Admin')
        self.assertEqual(department.company, company)
        self.assertEqual(department.employee_count(), 0)

    def test_employee_count(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        Employee.objects.create(company=company, department=department, name='John Doe', email='john@example.com', phone_number='1234567890', address='123 Street', job_title='HR Manager')
        self.assertEqual(department.employee_count(), 1)

class EmployeeModelTest(TestCase):
    def test_create_employee(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        employee = Employee.objects.create(company=company, department=department, name='John Doe', email='john@example.com', phone_number='1234567890', address='123 Street', job_title='HR Manager')
        self.assertEqual(employee.name, 'John Doe')
        self.assertEqual(employee.company, company)
        self.assertEqual(employee.department, department)
        self.assertEqual(employee.status, 'pending')
        self.assertIsNone(employee.work_days)  

    def test_work_days_calculation(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        hire_date = date(2023, 1, 1) 
        employee = Employee.objects.create(
            company=company,
            department=department,
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            address='123 Street',
            job_title='HR Manager',
            hire_date=hire_date  
        )
        self.assertIsNotNone(employee.work_days)
        self.assertGreater(employee.work_days, 0)

    def test_clean_method(self):
        company1 = Company.objects.create(name='Test Company 1')
        company2 = Company.objects.create(name='Test Company 2')
        department = Department.objects.create(company=company1, name='Admin')
        employee = Employee(company=company2, department=department, name='John Doe', email='john@example.com', phone_number='1234567890', address='123 Street', job_title='HR Manager')
        with self.assertRaises(ValueError):
            employee.clean() 




















# Integration Tests
class CompanyDepartmentIntegrationTest(TestCase):
    def test_company_department_interaction(self):
        company = Company.objects.create(name='Test Company')
        self.assertEqual(company.department_count(), 0)
        
        department = Department.objects.create(company=company, name='Admin')
        
        self.assertEqual(department.company, company)
        
        self.assertEqual(company.department_count(), 1)


class DepartmentEmployeeIntegrationTest(TestCase):
    def test_department_employee_interaction(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        
        self.assertEqual(department.employee_count(), 0)
        
        employee = Employee.objects.create(
            company=company,
            department=department,
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            address='123 Street',
            job_title='HR Manager',
            hire_date=date(2023, 1, 1)
        )
        
        self.assertEqual(employee.department, department)
        
        self.assertEqual(department.employee_count(), 1)

class CompanyEmployeeIntegrationTest(TestCase):
    def test_company_employee_interaction(self):
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        
        self.assertEqual(company.employee_count(), 0)
        
        employee = Employee.objects.create(
            company=company,
            department=department,
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            address='123 Street',
            job_title='HR Manager',
            hire_date=date(2023, 1, 1)
        )
        
        self.assertEqual(employee.company, company)
        
        self.assertEqual(company.employee_count(), 1)

class UserEmployeeIntegrationTest(TestCase):
    def test_user_employee_interaction(self):
        user = User.objects.create_user(email='manager@example.com', password='password123', role='manager')
        
        company = Company.objects.create(name='Test Company')
        department = Department.objects.create(company=company, name='Admin')
        
        employee = Employee.objects.create(
            company=company,
            department=department,
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            address='123 Street',
            job_title='HR Manager',
            hire_date=date(2023, 1, 1)
        )
        
        self.assertEqual(employee.name, 'John Doe')
        self.assertEqual(employee.company, company)
        self.assertEqual(employee.department, department)

class FullWorkflowIntegrationTest(TestCase):
    def test_full_workflow(self):
        user = User.objects.create_user(email='admin@example.com', password='admin123', role='admin')
        
        company = Company.objects.create(name='Test Company')
        
        self.assertEqual(company.department_count(), 0)
        self.assertEqual(company.employee_count(), 0)
        
        department = Department.objects.create(company=company, name='Admin')
        
        self.assertEqual(company.department_count(), 1)
        
        employee = Employee.objects.create(
            company=company,
            department=department,
            name='John Doe',
            email='john@example.com',
            phone_number='1234567890',
            address='123 Street',
            job_title='HR Manager',
            hire_date=date(2023, 1, 1)
        )
        
        self.assertEqual(company.employee_count(), 1)
        self.assertEqual(department.employee_count(), 1)
        
        self.assertEqual(employee.company, company)
        self.assertEqual(employee.department, department)