# Employee Management System

## Overview

The **Employee Management System** is a RESTful API built using Django and Django REST Framework (DRF). The system manages users, companies, departments, and employees, with role-based access control. It provides authentication using Django Token Authentication and includes API documentation via Swagger.

## Features

- User authentication and token-based authorization
- Role-based access control (Admin, Manager, Employee)
- CRUD operations for users, companies, departments, and employees
- Custom user model with email-based authentication
- API documentation using Swagger

## Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Authentication:** Django Token Authentication
- **Database:** PostgreSQL (or SQLite for development)
- **Documentation:** Swagger (drf-yasg)

---

## Project Setup

### Prerequisites

Ensure you have the following installed:

- Python 3.8+
- PostgreSQL (if using in production)
- Virtual environment (recommended)

### Installation Steps

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/ZAHERKRYEM/employee_M_back.git
   cd employee_M_back
   ```

2. **Create and Activate Virtual Environment:**

   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply Migrations:**

   ```sh
   python manage.py migrate
   ```

5. **Create a Superuser:**

   ```sh
   python manage.py createsuperuser
   ```

   Follow the prompts to set up an admin user.

6. **Run the Development Server:**

   ```sh
   python manage.py runserver
   ```

   The API will be available at `http://127.0.0.1:8000/api/`.

---

## API Endpoints

### Authentication

| Endpoint           | Method | Description                            |
| ------------------ | ------ | -------------------------------------- |
| `/api/token-auth/` | POST   | Authenticate a user and return a token |
| `/api/logout/`     | POST   | Logout a user by deleting the token    |

### User Management

| Endpoint           | Method    | Description                 |
| ------------------ | --------- | --------------------------- |
| `/api/users/`      | GET       | List all users (Admin only) |
| `/api/users/{id}/` | GET       | Retrieve a specific user    |
| `/api/users/`      | POST      | Create a new user           |
| `/api/users/{id}/` | PUT/PATCH | Update a user               |
| `/api/users/{id}/` | DELETE    | Delete a user (Admin only)  |

### Company Management

| Endpoint               | Method    | Description                       |
| ---------------------- | --------- | --------------------------------- |
| `/api/companies/`      | GET       | List all companies                |
| `/api/companies/{id}/` | GET       | Retrieve a specific company       |
| `/api/companies/`      | POST      | Create a new company (Admin only) |
| `/api/companies/{id}/` | PUT/PATCH | Update a company                  |
| `/api/companies/{id}/` | DELETE    | Delete a company (Admin only)     |

### Department Management

| Endpoint                 | Method    | Description                             |
| ------------------------ | --------- | --------------------------------------- |
| `/api/departments/`      | GET       | List all departments                    |
| `/api/departments/{id}/` | GET       | Retrieve a specific department          |
| `/api/departments/`      | POST      | Create a new department (Admin/Manager) |
| `/api/departments/{id}/` | PUT/PATCH | Update a department                     |
| `/api/departments/{id}/` | DELETE    | Delete a department (Admin only)        |

### Employee Management

| Endpoint               | Method    | Description                           |
| ---------------------- | --------- | ------------------------------------- |
| `/api/employees/`      | GET       | List all employees                    |
| `/api/employees/{id}/` | GET       | Retrieve a specific employee          |
| `/api/employees/`      | POST      | Create a new employee (Manager/Admin) |
| `/api/employees/{id}/` | PUT/PATCH | Update an employee                    |
| `/api/employees/{id}/` | DELETE    | Delete an employee (Manager/Admin)    |

---

## Security Measures

- **Token-based Authentication**: Each user receives a token upon login to ensure secure API access.
- **Role-Based Permissions**:
  - **Admin**: Full access to all operations.
  - **Manager**: Can manage departments and employees.
  - **Employee**: Can only view limited data.
- **Input Validation**: Regular expressions are used to validate phone numbers.
- **Password Hashing**: Passwords are securely hashed before storage.
- **Data Integrity Checks**: Ensures relationships between companies, departments, and employees are maintained.

---

## API Documentation

- Swagger UI is available at:
  ```sh
  http://127.0.0.1:8000/swagger/
  ```
  This interactive API documentation allows testing endpoints directly from the browser.

---

## Contribution Guide

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

---

## License

This project is licensed under the **EM License**. For more details, refer to the `LICENSE` file.

---

## Contact

For any questions or support, contact:

- **Email:** [zaherkryem@gmail.com](mailto\:zaherkryem@gmail.com)

