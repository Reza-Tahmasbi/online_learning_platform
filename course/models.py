from django.db import models
# from individuals.models import Student

# Create your models here.
class Course(models.Model):  
    
    LEVEL_BEGINNER = 'B'
    LEVEL_INTERMEDIATE = 'I'
    LEVEL_ADVANCED = 'A'
    
    LEVEL_CHOICES = [
        (LEVEL_BEGINNER, 'Beginner'),
        (LEVEL_INTERMEDIATE, 'Intermediate'),
        (LEVEL_ADVANCED, 'Advanced'),
    ]
    
    title = models.CharField(max_length = 150)
    description_text = models.CharField(max_length = 250)
    start_date = models.DateField()
    end_date = models.DateField(auto_now = True)
    level = models.CharField(max_length = 1, choices = LEVEL_CHOICES, default = LEVEL_BEGINNER)
    price = models.DecimalField(max_digits = 10, decimal_places = 2)
    language = models.CharField(max_length = 50)
    duration_hours = models.DecimalField(max_digits=5, decimal_places = 2) 
    thumbnail_url = models.URLField()
    
class CourseMaterials():
    MATERIAL_PDF = 'PDF'
    MATERIAL_RAR = 'RAR'
    MATERIAL_VIDEO = 'VIDEO'
    
    MATERIAL_CHOICES = [
        (MATERIAL_PDF, 'PDF'),
        (MATERIAL_RAR, 'RAR'),
        (MATERIAL_VIDEO, 'Video'),
    ]
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    material_type = models.CharField(max_length=100, choices = MATERIAL_CHOICES, default = MATERIAL_PDF)
    material_url = models.URLField()
    
    def __str__(self):
        return f"{self.course.title} - {self.get_material_type_display()}"
    
class Lesson():
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    title = models.CharField(max_length = 100)
    content = models.TextField()
    sequence_number = models.PositiveIntegerField()
    duration = models.DurationField(null=True, blank=True)
    is_published = models.BooleanField(default=False)   
    video_url = models.URLField()
    
    def __str__(self):
        return self.title
    
class Certificate():
    student = models.OneToOneField('Student', on_delete=models.CASCADE, related_name='certificate')
    title = models.CharField(max_length = 150)
    organization = models.CharField(max_length = 100)
    instructor_name = models.CharField(max_length = 100)
    # course = models.OneToOneField(Course, on_delete = models.CASCADE, primary_key = True)
    issue_date = models.DateField(auto_now = True)
    template = models.URLField()