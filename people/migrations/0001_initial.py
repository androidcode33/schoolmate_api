# Generated by Django 3.2.15 on 2023-10-15 08:49

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'public"."people',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=100)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('student_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_people', to='people.people')),
            ],
            options={
                'db_table': 'public"."student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('teacher_people', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_people', to='people.people')),
            ],
            options={
                'db_table': 'public"."teacher',
            },
        ),
        migrations.CreateModel(
            name='TeacherStudents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('student_teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_teacher', to='people.student')),
                ('teacher_students', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_students', to='people.teacher')),
            ],
            options={
                'db_table': 'public"."teacher_student',
            },
        ),
    ]