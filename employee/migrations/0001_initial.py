# Generated by Django 3.2.6 on 2021-09-23 10:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_designation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qualification_name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Employee_Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Employee_name', models.CharField(max_length=100)),
                ('Emp_mobile_no', models.CharField(max_length=120)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Shemale', 'Shemale'), ('Other', 'Other')], max_length=90)),
                ('Cnic', models.IntegerField()),
                ('Hire_date', models.DateField(blank=True, null=True)),
                ('End_date', models.DateField(blank=True, null=True)),
                ('Basic_salary', models.IntegerField()),
                ('Account_no', models.IntegerField()),
                ('Address', models.TextField()),
                ('Status', models.CharField(choices=[('Single', 'Single'), ('Married', 'Married')], max_length=120)),
                ('Picture', models.ImageField(upload_to='media')),
                ('Category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee_category')),
                ('Designation_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee_designation')),
                ('Qualification_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee_qualification')),
            ],
        ),
    ]
