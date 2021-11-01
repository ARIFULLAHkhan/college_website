from django.db import models

# Create your models here.

# Student Information Table

class Student_information(models.Model):
	CATEGORY = (
		('Pakistani', 'Pakistani'),
		('Indian', 'Indian'),
		('Other', 'Other'),
	)
	CATEGORY_2 = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
	CATEGORY_22 = (
		('Male', 'Male'),
		('Female', 'Female'),
		('Shemale', 'Shemale'),
		('Other', 'Other'),
	)
	student_name = models.CharField(max_length=80)
	father_name = models.CharField(max_length=90, null=True, blank=True)
	gender = models.CharField(max_length=90, choices=CATEGORY_22)
	D_O_B = models.DateField()
	address = models.CharField(max_length=90, null=True, blank=True)
	admission_date = models.DateField(auto_now_add=True)
	nationality = models.CharField(max_length=20, choices=CATEGORY)
	registration_no = models.IntegerField(unique=True)
	cnic = models.IntegerField(unique=True)
	status = models.CharField(max_length=20,choices=CATEGORY_2)
	picture = models.ImageField(upload_to='media')

	def __str__(self):
		return self.student_name

# Batches Table

class Batches(models.Model):
	CATEGORY_3 = (
		('Morning', 'Morning'),
		('Evening', 'Evening'),
	)
	CATEGORY_4 = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
	batch_name = models.CharField(max_length=120)
	shift = models.CharField(max_length=20, choices=CATEGORY_3)
	start_date = models.DateField()
	end_date = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=20, choices=CATEGORY_4, null=True, blank=True)

	def __str__(self):
		return self.batch_name

class Class_registration(models.Model):
	class_name = models.CharField(max_length=120)
	admission_fee = models.IntegerField(null=True, blank=True)
	tution_fee = models.IntegerField(null=True, blank=True)
	extra_fine = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.class_name

class Student_class(models.Model):
	CATEGORY_5 = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
	student_id = models.ForeignKey(Student_information, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class_registration, on_delete=models.CASCADE)
	batch_id = models.ForeignKey(Batches, on_delete=models.CASCADE)
	enrolment_date = models.DateField()
	status = models.CharField(max_length=20, choices=CATEGORY_5, null=True, blank=True)
	remarks = models.CharField(max_length=120, null=True, blank=True)

class Subject_of_different_classes(models.Model):
	subject_name = models.CharField(max_length=120, null=True, blank=True)
	theory_marks = models.IntegerField(null=True, blank=True)
	passing_marks = models.IntegerField(null=True, blank=True)
	practical_marks = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.subject_name

class Class_subject(models.Model):
	class_id = models.ForeignKey(Class_registration, on_delete=models.CASCADE)
	subject_id = models.ForeignKey(Subject_of_different_classes, on_delete=models.CASCADE)

class Student_payment(models.Model):
	student_id = models.ForeignKey(Student_information, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class_registration, on_delete=models.CASCADE)
	payment_date = models.DateField(null=True, blank=True)
	amount = models.IntegerField(null=True, blank=True)
	slip_no = models.IntegerField(unique=True, null=True, blank=True)

class Student_fee_collection(models.Model):
	student_id = models.ForeignKey(Student_information, on_delete=models.CASCADE)
	fee_date = models.DateField()
	applied_fee = models.IntegerField()
	comments = models.TextField(null=True, blank=True)
	class_id = models.ForeignKey(Class_registration, on_delete=models.CASCADE)

class Exam_type(models.Model):
	exam_name = models.CharField(max_length=129)

	def __str__(self):
		return self.exam_name

class Student_exam(models.Model):
	CATEGORY_6 = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
	student_id = models.ForeignKey(Student_information, on_delete=models.CASCADE)
	class_id = models.ForeignKey(Class_registration, on_delete=models.CASCADE)
	batch_id = models.ForeignKey(Batches, on_delete=models.CASCADE)
	subject_id = models.ForeignKey(Class_subject, on_delete=models.CASCADE)
	obtained_marks = models.IntegerField()
	status = models.CharField(max_length=20, choices=CATEGORY_6, null=True, blank=True)
	exam_id = models.ForeignKey(Exam_type, on_delete=models.CASCADE)

class Add_hostel(models.Model):
	hostel_name = models.CharField(max_length=120)
	owner = models.CharField(max_length=120, null=True, blank=True)
	address = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.hostel_name

class Student_record_hostel(models.Model):
	hostel = models.ForeignKey(Add_hostel, on_delete=models.CASCADE)
	student_id = models.ForeignKey(Student_information, on_delete=models.CASCADE)

class Floors_of_hostels(models.Model):
	hostel_id = models.ForeignKey(Add_hostel, on_delete=models.CASCADE)
	floor_name = models.CharField(max_length=120)

	def __str__(self):
		return self.floor_name

class Room_type_hostel(models.Model):
	CATEGORY_7 = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
	room_type_name = models.CharField(max_length=120)
	status = models.CharField(max_length=20, choices=CATEGORY_7)

	def __str__(self):
		return self.room_type_name

class Room_of_hostel(models.Model):
	floor_id = models.ForeignKey(Floors_of_hostels, on_delete=models.CASCADE)
	room_no = models.IntegerField(unique=True, null=True, blank=True)
	room_type_id = models.ForeignKey(Room_type_hostel, on_delete=models.CASCADE)

class Allotment_of_room(models.Model):
	CATEGORY_8 = (
		('Active', 'Active'),
		('Inactive', 'Inactive'),
	)
	student_id = models.ForeignKey(Student_information, on_delete=models.CASCADE)
	room_id = models.ForeignKey(Room_of_hostel, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=CATEGORY_8, null=True, blank=True)
	details = models.TextField(null=True, blank=True)

