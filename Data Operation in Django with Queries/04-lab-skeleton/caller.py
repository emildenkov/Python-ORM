import os
import uuid

import django


# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Student

"""
FC5204 John Doe 15/05/1995 john.doe@university.com

FE0054 Jane Smith null jane.smith@university.com

FH2014 Alice Johnson 10/02/1998 alice.johnson@university.com

FH2015 Bob Wilson 25/11/1996 bob.wilson@university.com
"""


def add_students():
    Student.objects.create(
        student_id='FC5204',
        first_name='John',
        last_name='Doe',
        birth_date='1995-05-15',
        email='john.doe@university.com'
    )

    Student.objects.create(
        student_id='FE0054',
        first_name='Jane',
        last_name='Smith',
        email='jane.smith@university.com'
    )

    Student.objects.create(
        student_id='FH2014',
        first_name='Alice',
        last_name='Johnson',
        birth_date='1998-02-10',
        email='alice.johnson@university.com'
    )

    Student.objects.create(
        student_id='FH2015',
        first_name='Bob',
        last_name='Wilson',
        birth_date='1996-11-25',
        email='bob.wilson@university.com'
    )


def get_students_info():
    students = Student.objects.all()
    students_info = []

    for student in students:
        students_info.append(f'Student №{student.student_id}: '
                             f'{student.first_name} {student.last_name};'
                             f' Email: {student.email}')

    return '\n'.join(students_info)


def update_students_emails():
    students = Student.objects.all()

    for student in students:
        student.email = student.email.replace(student.email.split('@')[1], 'uni-students.com')
        student.save()


def truncate_students():
    students = Student.objects.all().delete()
