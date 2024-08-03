import os
import django

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()


from main_app.models import Lecturer, LecturerProfile

# Keep the data from the previous exercises, so you can reuse it

lecturer = Lecturer.objects.get(first_name='John', last_name="Doe")
lecturer_profile = LecturerProfile.objects.create(lecturer=lecturer, email="john.doe@university.lecturers.com", bio="A skilled and passionate math lecturer", office_location="Sofia, Al. Stamobolyiski Str, Faculty of Mathematics and Computer Science, Room 101")

lecturer_profile_from_db = LecturerProfile.objects.get(email='john.doe@university.lecturers.com')

print(f"{lecturer_profile_from_db.lecturer.first_name} {lecturer_profile_from_db.lecturer.last_name} has a profile.")


