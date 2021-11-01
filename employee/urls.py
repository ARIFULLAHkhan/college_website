from django.urls import path
from . import views

urlpatterns = [
	path('', views.employee_home, name='employee_home'),
	path('add_category/', views.add_category, name='add_category'),
	path('employee_designation/', views.employee_designation, name='employee_designation'),
	path('add_qualification/', views.add_qualification, name='add_qualification'),
	path('employee_information/', views.employee_information, name='employee_information'),
	path('add_employee/', views.add_employee, name='add_employee'),
	path('employee_remove/<str:pk>/', views.employee_remove, name='employee_remove'),
	path('employee_update/<str:pk>/', views.employee_update, name='employee_update'),
	path('category_remove/<str:pk>/', views.category_remove, name='category_remove'),
	path('category_update/<str:pk>/', views.category_update, name='category_update'),
	path('designation_remove/<str:pk>/', views.designation_remove, name='designation_remove'),
	path('designation_update/<str:pk>/', views.designation_update, name='designation_update'),
	path('qualification_remove/<str:pk>/', views.qualification_remove, name='qualification_remove'),
	path('qualification_update/<str:pk>/', views.qualification_update, name='qualification_update'),
]
