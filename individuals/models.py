from django.db import models
from course.models import Course


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 150, unique = True, primary_key = True)
    email = models.EmailField(unique = True)
    password = models.CharField(max_length = 128)
    profile_iamge_url = models.URLField()
    registration_date = models.DateTimeField()
    last_login_date = models.DateTimeField(auto_now = True)
    bio = models.TextField(blank = True)
    country = models.CharField(max_length = 100, blank = True)
    
    class Meta:
        abstract = True
        
    def __str__(self):
        return self.username
    
class Student(User):
    courses_enrolled = models.ManyToManyField(Course, related_name ='Enrollment')
    courses_finished = models.ManyToManyField(Course, related_name ='Finished')

    def __str__(self):
        return f"{self.username} (Student ID: {self.student_id})"
    
class Instructor(User):
    expertise = models.CharField(max_length=100, blank=True)
    courses_taught = models.ManyToManyField(Course, related_name ='taught')

    def __str__(self):
        return self.username