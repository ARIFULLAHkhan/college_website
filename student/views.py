from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student_information, Student_fee_collection, Student_class, Student_exam, Exam_type, Student_exam, Student_record_hostel, Add_hostel, Floors_of_hostels, Room_type_hostel, Room_of_hostel, Allotment_of_room, Batches, Class_registration,Student_class,Subject_of_different_classes,Class_subject, Student_payment
from employee.models import Employee_Information
from .forms import StudentForm, ExamForm, ExamType, HostelForm, StudentRecordHostelForm, HostelFloorForm, RoomTypeForm, RoomOfHostelForm, AllotementRoomForm,BatchForm,RegistrationForm, StudentClassForm,SubjectInfoForm, AssignClassForm, StudentPayment,StudentFeeForm
from django.contrib import messages

# Create your views here.
def home_page(request):
	student_count = Student_information.objects.all().count()
	employee_count = Employee_Information.objects.all().count()
	active_student = Student_information.objects.filter(status='Active').count()
	inactive_student = Student_information.objects.filter(status='Inactive').count()
	data = {'student_count': student_count, 'employee_count': employee_count,
			'active_student': active_student, 'inactive_student': inactive_student}
	return render(request,'student_templates/home.html', data)

def student_home(request):
	return render(request, 'student_templates/student_home.html')

def student_info(request):
	query_list = Student_information.objects.all()
	data = {'all_students': query_list}
	return render(request, 'student_templates/student_info.html', data)

def search(request):
	query_list = Student_information.objects.all()

	if 'get_student' in request.GET:
		get_student = request.GET['get_student']
		if get_student:
			query_list = query_list.filter(student_name__icontains=get_student)

	data = {'all_students': query_list}

	return render(request, 'student_templates/search.html', data)

def add_student(request):
	student_form = StudentForm()
	if request.method == 'POST':
		student_form = StudentForm(request.POST, request.FILES)
		if student_form.is_valid():
			student_form.save()
			student_name = student_form.cleaned_data.get('student_name')
			messages.success(request, f"User Added Successfully: ( {student_name} )")
			return redirect('student_info')
		else:
			student_name = student_form.cleaned_data.get('student_name')
			messages.error(request, f'Added Student Failed: ( {student_name} )')
			return redirect('student_info')
	data = {'student_form': student_form}
	return render(request, 'student_templates/add_student.html', data)

def student_update(request, pk):
	select_student = Student_information.objects.get(id=pk)
	student_form = StudentForm(instance=select_student)
	if request.method == 'POST':
		select_student = StudentForm(request.POST, request.FILES, instance=select_student)
		if select_student.is_valid():
			select_student.save()
			student_name = select_student.cleaned_data.get('student_name')
			messages.warning(request, f'Student Updated Successfully : ( {student_name} )')
			return redirect('student_info')
		else:
			student_name = student_form.cleaned_data.get('student_name')
			messages.warning(request, f'Student Updated Failed: ( {student_name} )')
			return redirect('student_info')
	data = {'student_form': student_form}
	return render(request, 'student_templates/student_update.html', data)

def student_remove(request, pk):
	get_student=Student_information.objects.get(id=pk)
	if request.method == 'POST':
		student_name = get_student.student_name
		messages.error(request, f'Student Deleted : ( {student_name} )')
		get_student.delete()
		return redirect('student_info')
	data = {'get_student': get_student}
	return render(request, 'student_templates/student_delete.html', data)

def student_single_info(request, pk):
	get_single_student_info = Student_information.objects.get(id=pk)
	data = {'get_single_student_info': get_single_student_info}
	return render(request, 'student_templates/student_single_info.html', data)

def exam(request):
	return render(request, 'student_templates/student_exame.html')


def student_exam_type_show(request):
	exam_type=ExamType()
	all_exam=Exam_type.objects.all()
	if request.method == 'POST':
		exam_type = ExamType(request.POST)
		if exam_type.is_valid():
			exam_type.save()
			exam_name = exam_type.cleaned_data.get('exam_name')
			messages.success(request, f'Exam Type Added Successfully : ( {exam_name} )')
			return redirect('student_exam_type_show')
		else:
			return HttpResponse("Failed...")
	data= {'all_exam': all_exam, 'exam_type': exam_type}
	return render(request, 'student_templates/student_exam_type.html',data)


def student_exam_remove(request, pk):
	get_exam = Exam_type.objects.get(id=pk)
	exam_name = get_exam.exam_name
	get_exam.delete()
	messages.error(request, f'Exam Type Deleted : ( {exam_name} )')
	return redirect('student_exam_type_show')

def student_exam_update(request, pk):
	get_exam = Exam_type.objects.get(id=pk)
	exam_type=ExamType(instance=get_exam)
	if request.method == 'POST':
		exam_type = ExamType(request.POST, instance=get_exam)
		if exam_type.is_valid():
			exam_name = get_exam.exam_name
			exam_type.save()
			messages.warning(request, f'Exam Type Updated : ( {exam_name} )')
			return redirect('student_exam_type_show')
		else:
			return HttpResponse("Failed...")
	data= {'exam_type': exam_type}
	return render(request, 'student_templates/student_exam_update.html', data)

def student_exam(request):
	all_student_exam = Student_exam.objects.all()
	data = {'all_student_exam': all_student_exam}
	return render(request, 'student_templates/student_exam.html', data)

def add_student_exam(request):
	exame_form = ExamForm()
	if request.method == 'POST':
		exame_form = ExamForm(request.POST)
		if exame_form.is_valid():
			exame_form.save()
			messages.success(request, 'Student Exam Added Successfully...')
			return redirect('student_exam')
		else:
			return HttpResponse("Failed...")
	data = {'exame_form':exame_form}
	return render(request, 'student_templates/add_student_exam.html', data)

def delete_exame(request, pk):
	get_exam=Student_exam.objects.get(id=pk)
	if request.method=='POST':
		get_exam.delete()
		messages.error(request, 'Student Exam Deleted...')
		return redirect('student_exam')
	return render(request, 'student_templates/delete_exam.html')


def update_exam(request, pk):
	select_exam=Student_exam.objects.get(id=pk)
	exame_form=ExamForm(instance=select_exam)
	if request.method=='POST':
		exame_form=ExamForm(request.POST,instance=select_exam)
		if exame_form.is_valid():
			exame_form.save()
			messages.warning(request, 'Student Exam Updated...')
			return redirect('student_exam')
		else:
			return HttpResponse("updation is Failed")
	data={'exame_form':exame_form}
	return render(request,'student_templates/update_exam.html',data)

	


# Hostel Functions

def hostels(request):
	return render(request, 'hostel_templates/student_hostel_info.html')

def add_hostel(request):
	all_hostels = Add_hostel.objects.all()
	hostel_form = HostelForm()
	if request.method == 'POST':
		hostel_form = HostelForm(request.POST)
		if hostel_form.is_valid():
			hostel_form.save()
			messages.success(request, 'Hostel Added Successfully...')
			return redirect('add_hostel')
		else:
			return HttpResponse("failed...")
	data = {'all_hostels': all_hostels, 'hostel_form': hostel_form}
	return render(request, 'hostel_templates/add_hostel.html', data)

def delete_hostel(request, pk):
	get_hostel = Add_hostel.objects.get(id=pk)
	get_hostel.delete()
	messages.error(request, 'Hostel Deleted...')
	return redirect('add_hostel')

def update_hostel(request, pk):
	get_hostel = Add_hostel.objects.get(id=pk)
	hostel_form = HostelForm(instance=get_hostel)
	if request.method == 'POST':
		hostel_form = HostelForm(request.POST, instance=get_hostel)
		if hostel_form.is_valid():
			hostel_form.save()
			messages.warning(request, 'Hostel Updated...')
			return redirect('add_hostel')
		else:
			return HttpResponse("Error...")
	data = {'hostel_form': hostel_form}
	return render(request, 'hostel_templates/update_hostel.html', data)


def student_record_hostel(request):
	all_student_hostel = Student_record_hostel.objects.all()
	student_record_hostel_form = StudentRecordHostelForm()
	if request.method == 'POST':
		student_record_hostel_form = StudentRecordHostelForm(request.POST)
		if student_record_hostel_form.is_valid():
			student_record_hostel_form.save()
			messages.success(request, 'Student Record Added Successfully...')
			return redirect('student_record_hostel')
		else:
			return HttpResponse("Failed...")
	data = {'all_student_hostel': all_student_hostel, 'student_record_hostel_form': student_record_hostel_form}
	return render(request, 'hostel_templates/student_record_hostel.html', data)

def delete_student_hostel_record(request, pk):
	get_record = Student_record_hostel.objects.get(id=pk)
	get_record.delete()
	messages.error(request, 'Student Record in Hostel Deleted...')
	return redirect('student_record_hostel')

def update_student_hostel_record(request, pk):
	get_record = Student_record_hostel.objects.get(id=pk)
	student_record_hostel_form = StudentRecordHostelForm(instance=get_record)
	if request.method == 'POST':
		student_record_hostel_form = StudentRecordHostelForm(request.POST, instance=get_record)
		if student_record_hostel_form.is_valid():
			student_record_hostel_form.save()
			messages.warning(request, 'Student Record Updated...')
			return redirect('student_record_hostel')
		else:
			return HttpResponse("Fail...")
	data = {'student_record_hostel_form': student_record_hostel_form}
	return render(request, 'hostel_templates/update_student_hostel_record.html', data)

def floor_of_hostel(request):
	all_floor=Floors_of_hostels.objects.all()
	floor_form = HostelFloorForm()
	if request.method == 'POST':
		floor_form = HostelFloorForm(request.POST)
		if floor_form.is_valid():
			floor_form.save()
			messages.success(request, 'Hostel Floor Added Successfully....')
			return redirect('floor_of_hostel')
		else:
			return HttpResponse("Failed...")
	data={'all_floor': all_floor, 'floor_form': floor_form}
	return render(request, 'hostel_templates/floor_of_hostel.html', data)


def delete_floor(request, pk):
	get_floor = Floors_of_hostels.objects.get(id=pk)
	get_floor.delete()
	messages.error(request, 'Floor Deleted...')
	return redirect('floor_of_hostel')

def update_floor(request, pk):
	get_floor = Floors_of_hostels.objects.get(id=pk)
	floor_form = HostelFloorForm(instance=get_floor)
	if request.method == 'POST':
		floor_form = HostelFloorForm(request.POST, instance=get_floor)
		if floor_form.is_valid():
			floor_form.save()
			messages.warning(request, 'Floor Updated...')
			return redirect('floor_of_hostel')
		else:
			return HttpResponse("Failed...")
	data={'floor_form': floor_form}
	return render(request, 'hostel_templates/update_floor.html', data)

def hostel_room_type(request):
	all_room_type = Room_type_hostel.objects.all()
	room_type_form = RoomTypeForm()
	if request.method == 'POST':
		room_type_form = RoomTypeForm(request.POST)
		if room_type_form.is_valid():
			room_type_form.save()
			messages.success(request, 'Hostel Room Type Added Successfully...')
			return redirect('hostel_room_type')
		else:
			return HttpResponse("Failed...")
	data = {'all_room_type': all_room_type, 'room_type_form': room_type_form}
	return render(request, 'hostel_templates/hostel_room_type.html', data)

def delete_hostel_room(request, pk):
	get_type = Room_type_hostel.objects.get(id=pk)
	get_type.delete()
	messages.error(request, 'Hostel Room Type Deleted...')
	return redirect('hostel_room_type')

def update_hostel_room(request, pk):
	get_type = Room_type_hostel.objects.get(id=pk)
	room_type_form = RoomTypeForm(instance=get_type)
	if request.method == 'POST':
		room_type_form = RoomTypeForm(request.POST, instance=get_type)
		if room_type_form.is_valid():
			room_type_form.save()
			messages.warning(request, 'Hostel Room Type Updated...')
			return redirect('hostel_room_type')
		else:
			return HttpResponse("Error...")
	data = {'room_type_form': room_type_form}
	return render(request, 'hostel_templates/update_hostel_room.html', data)

def room_of_hostels(request):
	all_hostel_rooms = Room_of_hostel.objects.all()
	room_of_hostel_form = RoomOfHostelForm()
	if request.method == 'POST':
		room_of_hostel_form = RoomOfHostelForm(request.POST)
		if room_of_hostel_form.is_valid():
			room_of_hostel_form.save()
			messages.success(request, 'Room Of Hostel Added Successfully...')
			return redirect('room_of_hostels')
		else:
			return HttpResponse("Error...")
	data = {'all_hostel_rooms': all_hostel_rooms, 'room_of_hostel_form': room_of_hostel_form}
	return render(request, 'hostel_templates/room_of_hostel.html', data)

def delete_room_of_hostel(request, pk):
	get_room = Room_of_hostel.objects.get(id=pk)
	get_room.delete()
	messages.error(request, 'Room Of Hostel Deleted...')
	return redirect('room_of_hostels')

def allotment_of_room(request):
	all_allotement = Allotment_of_room.objects.all()
	allotment_room_form = AllotementRoomForm()
	if request.method == 'POST':
		allotment_room_form = AllotementRoomForm(request.POST)
		if allotment_room_form.is_valid():
			allotment_room_form.save()
			messages.success(request, 'Allotement Room Added Successfully...')
			return redirect('allotment_of_room')
		else:
			return HttpResponse("Error...")
	data = {'allotment_room_form': allotment_room_form, 'all_allotement': all_allotement}
	return render(request, 'hostel_templates/allotment_of_room.html', data)

def delete_allotment_of_room(request, pk):
	get_allotment = Allotment_of_room.objects.get(id=pk)
	get_allotment.delete()
	messages.error(request, 'Allotment Deleted...')
	return redirect('allotment_of_room')

def update_allotment_of_room(request, pk):
	get_allotment = Allotment_of_room.objects.get(id=pk)
	allotment_room_form = AllotementRoomForm(instance=get_allotment)
	if request.method == 'POST':
		allotment_room_form = AllotementRoomForm(request.POST, instance=get_allotment)
		if allotment_room_form.is_valid():
			allotment_room_form.save()
			messages.warning(request, 'Allotment Updated...')
			return redirect('allotment_of_room')
		else:
			return HttpResponse("Failed...")
	data = {'allotment_room_form': allotment_room_form}
	return render(request, 'hostel_templates/update_allotment_of_room.html', data)
#In This portion Student Batch is controlled.....
def batch_list(request):
	all_batches=Batches.objects.all()
	data={'all_batches':all_batches}
	return render(request, 'student_templates/batch_list.html', data)
def add_batch(request):
	batch_form=BatchForm()
	if request.method=='POST':
		batch_form=BatchForm(request.POST)
		if batch_form.is_valid():
			batch_form.save()
			return HttpResponse("Batch Added Successfully...")
		else:
			return HttpResponse("Sorry...")
	data={'batch_form':batch_form}
	return render(request, 'student_templates/add_batch.html', data)

def delete_batch(request, pk):
	get_batch=Batches.objects.get(id=pk)
	get_batch.delete()
	return redirect('batch_list')
def update_batch(request, pk):
	get_batch=Batches.objects.get(id=pk)
	batch_form=BatchForm(instance=get_batch)
	if request.method=='POST':
		batch_form=BatchForm(request.POST, instance=get_batch)
		if batch_form.is_valid():
			batch_form.save()
			return redirect('batch_list')
		else:
			return HttpResponse("Sorry...")
	data={'batch_form':batch_form}
	return render(request, 'student_templates/update_batch.html', data)
def class_registration_list(request):
	all_registration=Class_registration.objects.all()
	data={'all_registration':all_registration}
	return render(request, 'student_templates/class_registration_list.html',data)

def add_class_registration(request):
	registration_form=RegistrationForm()
	if request.method=='POST':
		registration_form=RegistrationForm(request.POST)
		if registration_form.is_valid():
			registration_form.save()
			return redirect('class_registration_list')
		else:
			return HttpResponse("Sorry...")
	data={'registration_form':registration_form}
	return render(request, 'student_templates/add_class_registration.html', data)


def delete_registration(request, pk):
	get_class=Class_registration.objects.get(id=pk)
	get_class.delete()
	return redirect('class_registration_list')

def update_registration(request,pk):
	get_class=Class_registration.objects.get(id=pk)
	registration_form=RegistrationForm(instance=get_class)
	if request.method=='POST':
		registration_form=RegistrationForm(request.POST, instance=get_class)
		if registration_form.is_valid():
			registration_form.save()
			return redirect('class_registration_list')
		else:
			return HttpResponse("Sorry...")
	data={'registration_form': registration_form}
	return render(request, 'student_templates/update_registration.html', data)


#student Class information


def student_class_list(request):
	get_student_class=Student_class.objects.all()
	data={'get_student_class':get_student_class}
	return render(request, 'student_templates/student_class_list.html', data)

def add_student_class(request):
	get_student_class_form=StudentClassForm()
	if request.method=='POST':
		get_student_class_form=StudentClassForm(request.POST)
		if get_student_class_form.is_valid():
			get_student_class_form.save()
			return redirect('student_class_list')
		else:
			return HttpResponse("Sorry...")
	data={'get_student_class_form':get_student_class_form}
	return render(request, 'student_templates/add_student_class.html', data)

def delete_student_class(request, pk):
	get_student_class=Student_class.objects.get(id=pk)
	get_student_class.delete()
	return redirect('student_class_list')
	
def update_student_class(request, pk):
	get_student_class=Student_class.objects.get(id=pk)
	get_student_class_form=StudentClassForm(instance=get_student_class)
	if request.method=='POST':
		get_student_class_form=StudentClassForm(request.POST, instance=get_student_class)
		if get_student_class_form.is_valid():
			get_student_class_form.save()
			return redirect('student_class_list')
		else:
			return HttpResponse("Sorry...")
	data={'get_student_class_form': get_student_class_form}
	return render(request, 'student_templates/update_student_class.html', data)


# Subject info
def subject_list_info(request):
	get_subject_list=Subject_of_different_classes.objects.all()
	data={'get_subject_list':get_subject_list}
	return render(request, 'student_templates/get_subject_list.html', data)


def add_subject_info(request):
	get_subject_form=SubjectInfoForm()
	if request.method=='POST':
		get_subject_form=SubjectInfoForm(request.POST)
		if get_subject_form.is_valid():
			get_subject_form.save()
			return redirect('subject_list_info')
		else:
			return HttpResponse('Sorry...')
	data={'get_subject_form': get_subject_form}
	return render(request, 'student_templates/add_subject_info.html', data)

def delete_subject_info(request, pk):
	get_subject_info=Subject_of_different_classes.objects.get(id=pk)
	get_subject_info.delete()
	return redirect('subject_list_info')

def update_subject_info(request, pk):
	get_subject_info=Subject_of_different_classes.objects.get(id=pk)
	get_subject_form=SubjectInfoForm(instance=get_subject_info)
	if request.method=='POST':
		get_subject_form=SubjectInfoForm(request.POST, instance=get_subject_info)
		if get_subject_form.is_valid():
			get_subject_form.save()
			return redirect('subject_list_info')
		else:
			return HttpResponse("Sorry...")
	data={'get_subject_form':get_subject_form}
	return render(request, 'student_templates/update_subject_info.html', data)

def assign_class_list(request):
	get_class_subject=Class_subject.objects.all()
	data={'get_class_subject': get_class_subject}
	return render(request, 'student_templates/assign_class_list.html', data)

def add_class_subject(request):
	class_subject_form=AssignClassForm()
	if request.method=='POST':
		class_subject_form=AssignClassForm(request.POST)
		if class_subject_form.is_valid():
			class_subject_form.save()
			return redirect('assign_class_list')
		else:
			return HttpResponse('Sorry...')
	data={'class_subject_form':class_subject_form}
	return render(request, 'student_templates/add_class_subject.html', data)

def delete_class_subject(request,pk):
	get_class_subject=Class_subject.objects.get(id=pk)
	get_class_subject.delete()
	return redirect('assign_class_list')

def update_class_subject(request, pk):
	get_class_subject=Class_subject.objects.get(id=pk)
	class_subject_form=AssignClassForm(instance=get_class_subject)
	if request.method=='POST':
		class_subject_form=AssignClassForm(request.POST, instance=get_class_subject)
		if class_subject_form.is_valid():
			class_subject_form.save()
			return redirect('assign_class_list')
		else:
			return HttpResponse('Sorry...')
	data={'class_subject_form':class_subject_form}
	return render(request, 'student_templates/update_class_subject.html', data)


def student_payment_list(request):
	get_payment_list=Student_payment.objects.all()
	data={'get_payment_list':get_payment_list}
	return render(request, 'student_templates/student_payment_list.html', data)

def add_student_payment(request):
	get_payment_form=StudentPayment()
	if request.method=='POST':
		get_payment_form=StudentPayment(request.POST)
		if get_payment_form.is_valid():
			get_payment_form.save()
			return redirect('student_payment_list')
		else:
			return HttpResponse("Sorry...")
	data={'get_payment_form': get_payment_form}
	return render(request, 'student_templates/add_student_payment.html', data)

def delete_payment(request, pk):
	get_payment=Student_payment.objects.get(id=pk)
	get_payment.delete()
	return redirect('student_payment_list')

def update_payment(request, pk):
	get_payment=Student_payment.objects.get(id=pk)
	get_payment_form=StudentPayment(instance=get_payment)
	if request.method=='POST':
		get_payment_form=StudentPayment(request.POST, instance=get_payment)
		if get_payment_form.is_valid():
			get_payment_form.save()
			return redirect('student_payment_list')
		else:
			return HttpResponse("Sorry...")
	data={'get_payment_form':get_payment_form}
	return render(request, 'student_templates/update_payment.html', data)


def student_fee_list(request):
	get_student_fee=Student_fee_collection.objects.all()
	data={'get_student_fee':get_student_fee}
	return render(request,'student_templates/student_fee_list.html', data)

def add_student_fee(request):
	get_fee_form=StudentFeeForm()
	if request.method=='POST':
		get_fee_form=StudentFeeForm(request.POST)
		if get_fee_form.is_valid():
			get_fee_form.save()
			return redirect('student_fee_list')
		else:
			return HttpResponse('Sorry...')
	data={'get_fee_form':get_fee_form}
	return render(request, 'student_templates/add_student_fee.html', data)


def delete_student_fee(request, pk):
	get_student_fee=Student_fee_collection.objects.get(id=pk)
	get_student_fee.delete()
	return redirect('student_fee_list')

def update_student_fee(request, pk):
	get_student_fee=Student_fee_collection.objects.get(id=pk)
	student_fee_form=StudentFeeForm(instance=get_student_fee)
	if request.method=='POST':
		student_fee_form=StudentFeeForm(request.POST, instance=get_student_fee)
		if student_fee_form.is_valid():
			student_fee_form.save()
			return redirect('student_fee_list')
		else:
			return HttpResponse('Sorry...')
	data={'student_fee_form':student_fee_form}
	return render(request, 'student_templates/update_student_fee.html', data)
