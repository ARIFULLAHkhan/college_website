from django import forms
from .models import Employee_Information, Employee_category, Employee_designation, Employee_Qualification

class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee_Information
		fields = '__all__'

		labels = {
			'Employee_name' : '',
			'Emp_mobile_no' : '',
			'Gender' : '',
			'Cnic' : '',
			'Hire_date' : '',
			'End_date' : '',
			'Basic_salary':'',
			'Account_no':'',
			'Address':'',
			'Status':'',
			'Picture':'',
		}

		widgets={
			'Employee_name': forms.TextInput(attrs={'placeholder':'Enter Employee name'}),
			'Emp_mobile_no': forms.TextInput(attrs={'placeholder':'Enter mobile number'}),
			'Cnic': forms.TextInput(attrs={'placeholder':'Enter national Id '}),
			'Hire_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
			'End_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
			'Basic_salary': forms.TextInput(attrs={'placeholder':'Enter Basic salary'}),
			'Account_no': forms.TextInput(attrs={'placeholder':'Enter Account No'}),
			'Address': forms.TextInput(attrs={'placeholder':'Enter your address'}),
		}

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Employee_category
		fields = '__all__'

		labels = {
		'category_name' : '',
		}

		widgets = {
		'category_name': forms.TextInput(attrs={'placeholder':'Enter Category Name'}),
		}

class DesignationForm(forms.ModelForm):
	class Meta:
		model = Employee_designation
		fields = '__all__'

		labels = {
		'designation_name' : '',
		}

		widgets = {
		'designation_name': forms.TextInput(attrs={'placeholder':'Enter Designation Name'}),
		}

class QualificationForm(forms.ModelForm):
	class Meta:
		model = Employee_Qualification
		fields = '__all__'

		labels = {
		'qualification_name' : '',
		}

		widgets = {
		'qualification_name': forms.TextInput(attrs={'placeholder':'Enter Qualification Name'}),
		}






