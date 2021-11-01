from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('student_home/', views.student_home, name='student_home'),
    path('student_info/', views.student_info, name='student_info'),
    path('student_single_info/<str:pk>/', views.student_single_info, name='student_single_info'),
    path('exam/',views.exam, name='exam'),
    path('student_exam_type_show/', views.student_exam_type_show, name='student_exam_type_show'),
    path('student_exam/', views.student_exam, name='student_exam'),

    # Path For Hostels
    path('hostels/', views.hostels, name='hostels'),
    path('add_hostel/', views.add_hostel, name='add_hostel'),
    path('student_record_hostel/', views.student_record_hostel, name='student_record_hostel'),
    path('floor_of_hostel/', views.floor_of_hostel, name='floor_of_hostel'),
    path('hostel_room_type/', views.hostel_room_type, name='hostel_room_type'),
    path('room_of_hostels/', views.room_of_hostels, name='room_of_hostels'),

    path('add_student/', views.add_student, name='add_student'),
    path('student_update/<str:pk>/', views.student_update, name='student_update'),
    path('student_remove/<str:pk>/', views.student_remove, name='student_remove'),
    path('add_student_exam/', views.add_student_exam, name='add_student_exam'),
    path('delete_exame/<str:pk>/', views.delete_exame, name='delete_exame'),
    path('update_exam/<str:pk>/', views.update_exam, name='update_exam'),
    path('student_exam_remove/<str:pk>/', views.student_exam_remove, name='student_exam_remove'),
    path('student_exam_update/<str:pk>/', views.student_exam_update, name='student_exam_update'),
    path('search/', views.search, name='search'),


    path('delete_hostel/<str:pk>/', views.delete_hostel, name='delete_hostel'),
    path('update_hostel/<str:pk>/', views.update_hostel, name='update_hostel'),

    path('delete_student_hostel_record/<str:pk>/', views.delete_student_hostel_record, name='delete_student_hostel_record'),
    path('update_student_hostel_record/<str:pk>/', views.update_student_hostel_record, name='update_student_hostel_record'),
    path('delete_floor/<str:pk>/', views.delete_floor, name='delete_floor'),
    path('update_floor/<str:pk>/', views.update_floor, name='update_floor'),
    path('delete_hostel_room/<str:pk>/', views.delete_hostel_room, name='delete_hostel_room'),
    path('update_hostel_room/<str:pk>/', views.update_hostel_room, name='update_hostel_room'),
    path('delete_room_of_hostel/<str:pk>/', views.delete_room_of_hostel, name='delete_room_of_hostel'),
    path('allotment_of_room/', views.allotment_of_room, name='allotment_of_room'),
    path('delete_allotment_of_room/<str:pk>', views.delete_allotment_of_room, name='delete_allotment_of_room'),
    path('update_allotment_of_room/<str:pk>/', views.update_allotment_of_room, name='update_allotment_of_room'),

    path('batch_list/', views.batch_list, name='batch_list'),
    path('add_batch/', views.add_batch, name='add_batch'),
    path('delete_batch/<str:pk>/', views.delete_batch, name='delete_batch'),
    path('update_batch/<str:pk>/', views.update_batch, name='update_batch'),

    path('class_registration_list/', views.class_registration_list, name='class_registration_list'),
    path('add_class_registration/', views.add_class_registration, name='add_class_registration'),
    path('delete_registration/<str:pk>/', views.delete_registration, name='delete_registration'),
    path('update_registration/<str:pk>/', views.update_registration, name='update_registration'),


    path('student_class_list/', views.student_class_list, name='student_class_list'),
    path('add_student_class/', views.add_student_class, name='add_student_class'),
    path('delete_student_class/<str:pk>/', views.delete_student_class, name='delete_student_class'),
    path('update_student_class/<str:pk>/', views.update_student_class, name='update_student_class'),

    path('subject_list_info/', views.subject_list_info, name='subject_list_info'),
    path('add_subject_info/', views.add_subject_info, name='add_subject_info'),
    path('delete_subject_info/<str:pk>/', views.delete_subject_info, name='delete_subject_info'),
    path('update_subject_info/<str:pk>/', views.update_subject_info, name='update_subject_info'),

    path('assign_class_list/', views.assign_class_list, name='assign_class_list'),
    path('add_class_subject/', views.add_class_subject, name='add_class_subject'),
    path('delete_class_subject/<str:pk>/', views.delete_class_subject, name='delete_class_subject'),
    path('update_class_subject/<str:pk>/', views.update_class_subject, name='update_class_subject'),

    path('student_payment_list/', views.student_payment_list, name='student_payment_list'),
    path('add_student_payment/', views.add_student_payment, name='add_student_payment'),
    path('delete_payment/<str:pk>/', views.delete_payment, name='delete_payment'),
    path('update_payment/<str:pk>/', views.update_payment, name='update_payment'),

    path('student_fee_list/', views.student_fee_list, name='student_fee_list'),
    path('add_student_fee/', views.add_student_fee, name='add_student_fee'),
    path('delete_student_fee/<str:pk>/', views.delete_student_fee, name='delete_student_fee'),
    path('update_student_fee/<str:pk>/', views.update_student_fee, name='update_student_fee'),


]










