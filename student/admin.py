from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Student_information)
admin.site.register(Batches)
admin.site.register(Class_registration)
admin.site.register(Student_class)
admin.site.register(Subject_of_different_classes)
admin.site.register(Class_subject)
admin.site.register(Student_payment)
admin.site.register(Student_fee_collection)
admin.site.register(Exam_type)
admin.site.register(Student_exam)

admin.site.register(Add_hostel)
admin.site.register(Student_record_hostel)
admin.site.register(Floors_of_hostels)
admin.site.register(Room_type_hostel)
admin.site.register(Room_of_hostel)
admin.site.register(Allotment_of_room)
