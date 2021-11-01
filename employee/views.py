from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Employee_category, Employee_designation, Employee_Qualification, Employee_Information
from .forms import EmployeeForm, CategoryForm, DesignationForm, QualificationForm
from django.core.paginator import Paginator

# Create your views here.

def employee_home(request):
	return render(request, 'employee/employee_home.html')

def employee_information(request):
	all_employee = Employee_Information.objects.all()
	paginator = Paginator(all_employee, 3)
	page = request.GET.get('page')
	page_listings = paginator.get_page(page)

	if 'get_employee' in request.GET:
		get_employee = request.GET['get_employee']
		if get_employee:
			page_listings = all_employee.filter(Employee_name__icontains=get_employee)

	data = {'all_employee': page_listings}
	return render(request, 'employee/employee_information.html', data)

def add_category(request):
	all_category = Employee_category.objects.all()
	category_form = CategoryForm()
	if request.method == 'POST':
		category_form = CategoryForm(request.POST)
		if category_form.is_valid():
			category_name = category_form.cleaned_data.get('category_name')
			category_form.save()
			messages.success(request, f'Category Added Successfully : ( {category_name} )')
			return redirect('add_category')
		else:
			return HttpResponse("Error")
	data = {'all_category': all_category, 'category_form': category_form}
	return render(request, 'employee/add_category.html', data)

def category_update(request, pk):
	get_category = Employee_category.objects.get(id=pk)
	category_form = CategoryForm(instance=get_category)
	if request.method == 'POST':
		category_form = CategoryForm(request.POST, instance=get_category)
		if category_form.is_valid():
			category_name = get_category.category_name
			category_form.save()
			messages.warning(request, f'Category Updated ( {category_name} ) ')
			return redirect('add_category')
	data = {'category_form': category_form}
	return render(request, 'employee/category_update.html', data)

def category_remove(request, pk):
	get_category = Employee_category.objects.get(id=pk)
	if request.method == 'POST':
		category_name = get_category.category_name
		get_category.delete()
		messages.error(request, f'Category Deleted : ( {category_name} )')
		return redirect('add_category')
	data = {'get_category': get_category}
	return render(request, 'employee/category_remove.html')

def employee_designation(request):
	all_designation = Employee_designation.objects.all()
	designation_form = DesignationForm()
	if request.method == 'POST':
		designation_form = DesignationForm(request.POST)
		if designation_form.is_valid():
			designation_name = designation_form.cleaned_data.get('designation_name')
			designation_form.save()
			messages.success(request, f'Designation Added Successfully : ( {designation_name} ) ')
			return redirect('employee_designation')
		else:
			return HttpResponse("Error")
	data = {'all_designation': all_designation, 'designation_form': designation_form}
	return render(request, 'employee/designation.html', data)

def designation_remove(request, pk):
	get_designation = Employee_designation.objects.get(id=pk)
	if request.method == 'POST':
		designation_name = get_designation.designation_name
		get_designation.delete()
		messages.error(request, f'Designation Deleted : ( {designation_name} )')
		return redirect('employee_designation')
	data = {'get_designation': get_designation}
	return render(request, 'employee/designation_remove.html', data)

def designation_update(request, pk):
	get_designation = Employee_designation.objects.get(id=pk)
	designation_form = DesignationForm(instance=get_designation)
	if request.method == 'POST':
		designation_form = DesignationForm(request.POST, instance=get_designation)
		if designation_form.is_valid():
			designation_name = get_designation.designation_name
			designation_form.save()
			messages.warning(request, f'Designation Updated : ( {designation_name} ) ')
			return redirect('employee_designation')
		else:
			return HttpResponse('Error')
	data = {'designation_form': designation_form}
	return render(request, 'employee/designation_update.html', data)

def add_qualification(request):
	all_qualification = Employee_Qualification.objects.all()
	qualification_form = QualificationForm()
	if request.method == 'POST':
		qualification_form = QualificationForm(request.POST)
		if qualification_form.is_valid():
			qualification_name = qualification_form.cleaned_data.get('qualification_name')
			qualification_form.save()
			messages.success(request, f'Data Added Successfully ( {qualification_name} ) ')
			return redirect('add_qualification')
		else:
			return HttpResponse("Fail")
	data = {'all_qualification': all_qualification, 'qualification_form': qualification_form}
	return render(request, 'employee/add_qualification.html', data)

def qualification_update(request, pk):
	get_qualification = Employee_Qualification.objects.get(id=pk)
	qualification_form = QualificationForm(instance=get_qualification)
	if request.method == 'POST':
		qualification_form = QualificationForm(request.POST, instance=get_qualification)
		if qualification_form.is_valid():
			qualification_name = get_qualification.qualification_name
			qualification_form.save()
			messages.warning(request, f'Qualfication Updated ( {qualification_name} ) ')
			return redirect('add_qualification')
		else:
			return HttpResponse('Error')
	data = {'qualification_form': qualification_form}
	return render(request, 'employee/qualification_update.html', data)

def qualification_remove(request, pk):
	get_qualification = Employee_Qualification.objects.get(id=pk)
	if request.method == 'POST':
		qualification_name = get_qualification.qualification_name
		get_qualification.delete()
		messages.error(request, f'Qualfication Deleted ( {qualification_name} ) ')
		return redirect('add_qualification')
	data = {'get_qualification': get_qualification}
	return render(request, 'employee/qualification_remove.html', data)

def add_employee(request):
	employe_form=EmployeeForm()
	if request.method=='POST':
		employe_form=EmployeeForm(request.POST, request.FILES)
		if employe_form . is_valid():
			employee_name = employe_form.cleaned_data.get('Employee_name')
			employe_form.save()
			messages.success(request, f'Employee Added Successfully ( {employee_name} )')
			return redirect('employee_information')
		else:
			messages.error(request, 'Employee Added Fail...')
			return redirect('add_employee')
	data={'employe_form':employe_form}
	return render(request, 'employee/add_employee.html',data)

def employee_update(request, pk):
	get_employee = Employee_Information.objects.get(id=pk)
	employee_form=EmployeeForm(instance=get_employee)
	if request.method == 'POST':
		employe_form = EmployeeForm(request.POST, request.FILES, instance=get_employee)
		if employe_form.is_valid():
			employee_name = employe_form.cleaned_data.get('Employee_name')
			employe_form.save()
			messages.warning(request, f'Employee Updated Successfully ( {employee_name} )')
			return redirect('employee_information')
		else:
			return HttpResponse("Fail...")
	data = {'employe_form': employee_form}
	return render(request, 'employee/employee_update.html', data)

def employee_remove(request, pk):
	get_employee = Employee_Information.objects.get(id=pk)
	if request.method == 'POST':
		get_employee.delete()
		student_name = get_employee.Employee_name
		messages.error(request, f'Employee Deleted : ( {student_name} )')
		return redirect('employee_information')
	data = {'get_employee': get_employee}
	return render(request, 'employee/employee_remove.html', data)





