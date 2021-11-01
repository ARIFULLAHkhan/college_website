from django import forms
from .models import Student_information, Student_exam, Exam_type, Add_hostel, Student_record_hostel, Floors_of_hostels, Room_type_hostel, Room_of_hostel, Allotment_of_room, Batches, Class_registration, Student_class,Subject_of_different_classes,Class_subject,Student_payment,Student_fee_collection
class StudentForm(forms.ModelForm):
	class Meta:
		model = Student_information
		fields = '__all__'

		labels = {
			'student_name' : '',
			'father_name' : '',
			'address' : '',
			'cnic' : '',
			'gender' : '',
			'student_name' : ''
		}

		widgets = {
            'student_name' :  forms.TextInput(attrs={'placeholder': 'Student Name'}),
            'father_name' :  forms.TextInput(attrs={'placeholder': 'Father Name'}),
            'address' :  forms.TextInput(attrs={'placeholder': 'Enter Address'}),
            'cnic' :  forms.TextInput(attrs={'placeholder': 'Enter CNIC without dashes'}),
            'registration_no' :  forms.TextInput(attrs={'placeholder': 'Enter Registration No'}),
            'D_O_B' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
		}

class ExamForm(forms.ModelForm):
	class Meta:
		model = Student_exam
		fields='__all__'



class ExamType(forms.ModelForm):
	class Meta:
		model= Exam_type
		fields='__all__'

		widgets = {
            'exam_name' :  forms.TextInput(attrs={'placeholder': 'Enter Exam Name'}),
		}


class HostelForm(forms.ModelForm):
	class Meta:
		model = Add_hostel
		fields = '__all__'

		widgets = {
            'hostel_name' :  forms.TextInput(attrs={'placeholder': 'Hostel Name'}),
            'owner' :  forms.TextInput(attrs={'placeholder': 'Owner Of Hostel'}),
            'address' :  forms.TextInput(attrs={'placeholder': 'Address Of Hostel'}),
		}

		labels = {
			'hostel_name' : '',
			'owner' : '',
			'address' : '',
		}

class StudentRecordHostelForm(forms.ModelForm):
	class Meta:
		model = Student_record_hostel
		fields = '__all__'

		labels = {
			'hostel' : 'Select Hostel',
			'student_id' : 'Select Student',
		}


class HostelFloorForm(forms.ModelForm):
	class Meta:
		model = Floors_of_hostels
		fields = '__all__'

		widgets = {
            'floor_name' :  forms.TextInput(attrs={'placeholder': 'Floor Name'}),
		}

		labels = {
			'hostel_id' : 'Select Hostel',
		}

class RoomTypeForm(forms.ModelForm):
	class Meta:
		model = Room_type_hostel
		fields = '__all__'

		widgets = {
            'room_type_name' :  forms.TextInput(attrs={'placeholder': 'Enter Room Type Name'}),
		}

		labels = {
			'room_type_name': '',
			'status' : 'Select Status',
		}

class RoomOfHostelForm(forms.ModelForm):
	class Meta:
		model = Room_of_hostel
		fields = '__all__'

		labels = {
			'floor_id': 'Select Floor',
			'room_type_id' : 'Select Room Type',
		}

class AllotementRoomForm(forms.ModelForm):
	class Meta:
		model = Allotment_of_room
		fields = '__all__'

		labels = {
			'student_id': 'Select Student',
			'room_id' : 'Select Room',
		}


class BatchForm(forms.ModelForm):
	class Meta:
		model=Batches
		fields= '__all__'

		widgets = {
            'start_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
            'end_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
		}

class RegistrationForm(forms.ModelForm):
	class Meta:
		model=Class_registration
		fields='__all__'


class StudentClassForm(forms.ModelForm):
	class Meta:
		model=Student_class
		fields='__all__'

		widgets = {
            'enrolment_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
            		}


class SubjectInfoForm(forms.ModelForm):
	class Meta:
		model=Subject_of_different_classes
		fields='__all__'


class AssignClassForm(forms.ModelForm):
	class Meta:
		model=Class_subject
		fields='__all__'

class StudentPayment(forms.ModelForm):
	class Meta:
		model=Student_payment
		fields='__all__'


		widgets = {
            'payment_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
            		}

class StudentFeeForm(forms.ModelForm):
	class Meta:
		model=Student_fee_collection
		fields='__all__'

		widgets = {
            'fee_date' : forms.DateInput(format=('%m%d%y'), attrs={'placeholder': 'Pick A Date', 'type': 'date'}),
            		}