from django.test import TestCase
from people.models import *

class PeopleTest(TestCase):
    """ Test module for People model """

    def setUp(self):
        # test student creation
        data = {"name":"Muhwezi Jerald"}
        student = People.objects.create(**data)

        if student:
            student = Student.objects.create(surname="Basasa", student_people=student)
        
        # test teacher creation
        data = {"name":"Namanya Ronald"}
        teacher = People.objects.create(**data)
        if teacher:
            teacher = Teacher.objects.create(teacher_people=teacher)

            # assign student to teacher
            TeacherStudents.objects.create(teacher_students=student, student_teacher=teacher)
    
    def test_people(self):
        people_student = Student.objects.filter(student_people__name='Muhwezi Jerald').first()
        people_teacher = Teacher.objects.filter(teacher_people__name='Namanya Ronald').first()
        teacher_students = TeacherStudents.objects.filter(teacher_students__teacher_people__name='Namanya Ronald', student_teacher__student_people__name='Muhwezi Jerald').first()

        self.assertEqual(people_student.student_people.name, "Muhwezi Jerald", "Student creation successful")
        self.assertEqual(people_teacher.teacher_people.name, "Namanya Ronald", "Teacher creation successful")
        self.assertEqual(len(teacher_students), 1, "Teacher - student assignment successful")
        
        