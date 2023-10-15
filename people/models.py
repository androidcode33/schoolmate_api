from django.db import models
from django.db import models
from django.utils import timezone

# people can be student/teacher
class People(models.Model):
    name =  models.CharField(max_length=100)
    date_added = models.DateTimeField(default = timezone.now)
    
    class Meta:
        db_table = 'public\".\"people'

class Student(models.Model):
    surname =  models.CharField(max_length=100)
    student_people = models.ForeignKey(People, on_delete=models.CASCADE, related_name='student_people')
    date_added = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'public\".\"student'

class Teacher(models.Model):
    teacher_people = models.ForeignKey(People, on_delete=models.CASCADE, related_name='teacher_people')
    date_added = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'public\".\"teacher'

class TeacherStudents(models.Model):
    teacher_students = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name='teacher_students')
    student_teacher = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student_teacher')
    date_added = models.DateTimeField(default = timezone.now)

    class Meta:
        db_table = 'public\".\"teacher_student'