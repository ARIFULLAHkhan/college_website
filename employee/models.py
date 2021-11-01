from django.db import models

# Write your model here.

class Employee_category(models.Model):
	category_name=models.CharField(max_length=120)
	
	def __str__(self):
		return self.category_name

class Employee_designation(models.Model):
	designation_name=models.CharField(max_length=120)
	
	def __str__(self):
		return self.designation_name

class Employee_Qualification(models.Model):
	qualification_name=models.CharField(max_length=120)
	
	def __str__(self):
		return self.qualification_name


class Employee_Information(models.Model):
	CATEGORY= (
		('Male', 'Male'),
		('Female', 'Female'),
		('Shemale', 'Shemale'),
		('Other', 'Other'),
	)
	CATEGORY_1=(
		('Single', 'Single'),
		('Married', 'Married')
		)
	Employee_name=models.CharField(max_length=100)
	Emp_mobile_no=models.CharField(max_length=120)
	Gender= models.CharField(max_length=90, choices=CATEGORY)
	Cnic=models.IntegerField()
	Hire_date=models.DateField(null=True, blank=True)
	End_date= models.DateField(null=True, blank=True)
	Basic_salary=models.IntegerField()
	Account_no=models.IntegerField()
	Address=models.TextField()
	Category_id=models.ForeignKey(Employee_category, on_delete=models.CASCADE)
	Designation_id=models.ForeignKey(Employee_designation, on_delete=models.CASCADE)
	Qualification_id=models.ForeignKey(Employee_Qualification, on_delete=models.CASCADE)
	Status=models.CharField(max_length=120, choices=CATEGORY_1)
	Picture=models.ImageField(upload_to='media')
	
	def __str__(self):
		return self.Employee_name


