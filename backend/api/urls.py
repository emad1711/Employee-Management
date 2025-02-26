from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
router.register(r'users', views.UserViewSet, basename='user')
router.register(r'companies', views.CompanyViewSet, basename='company')
router.register(r'departments', views.DepartmentViewSet, basename='department')
router.register(r'employees', views.EmployeeViewSet, basename='employee')

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token-auth/', views.custom_auth_token, name='token_auth'),
    path('api/logout/', views.logout_view, name='logout'), 

    path('swagger/', views.schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
