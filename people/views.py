from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *

class PeopleViewSet(viewsets.ModelViewSet):
    '''
    List all people
    '''
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend, )
    filterset_fields = ['name', 'id']
    search_fields = ('name', )
    ordering_fields = ['name', 'id' ]

class StudentsViewSet(viewsets.ModelViewSet):
    '''
    List all students
    '''
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend, )
    filterset_fields = ['surname', 'id']
    search_fields = ('surname', )
    ordering_fields = ['surname', 'id']

class TeachersViewSet(viewsets.ModelViewSet):
    '''
    List all teachers
    '''
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend, )
    filterset_fields = ['id']
    search_fields = ('id', )
    ordering_fields = ['id']