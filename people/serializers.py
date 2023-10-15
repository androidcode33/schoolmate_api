from rest_framework import serializers
from .models import *

class PeopleSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    date_added = serializers.CharField(read_only=True)
    
    class Meta:
        model = People
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    date_added = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, source="student_people.name")
    people_id = serializers.CharField(read_only=True, source="student_people.id")
    
    class Meta:
        model = Student
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    date_added = serializers.CharField(read_only=True)
    name = serializers.CharField(read_only=True, source="teacher_people.name")
    people_id = serializers.CharField(read_only=True, source="teacher_people.id")
    list_of_students = serializers.SerializerMethodField()
    
    class Meta:
        model = Teacher
        fields = '__all__'
    
    def get_list_of_students(self, obj):
        # returns the list of teacher's students
        students_list = []
        teacher_students = TeacherStudents.objects.filter(teacher_students=obj)
        for teacher_student in teacher_students:
            students_list.append({"id":teacher_student.student_teacher.id, "people_id":teacher_student.student_teacher.student_people.id, "name":teacher_student.student_teacher.student_people.name, "surname":teacher_student.student_teacher.surname})

        return students_list

class TeacherStudentsSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)
    date_added = serializers.CharField(read_only=True)
    
    class Meta:
        model = TeacherStudents
        fields = '__all__'