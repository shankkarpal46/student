from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=100,primary_key=True)
    student_image = models.ImageField(upload_to="students/")
    student_first_name = models.CharField(max_length = 100, null = False)
    student_middle_name = models.CharField(max_length = 100, null = False)
    student_last_name = models.CharField(max_length = 100, null = False)
    student_date_birth = models.DateField(null=True)
    student_address = models.TextField(default = "Please enter your address.")
    student_email = models.EmailField() 
    student_contact_number = models.PositiveBigIntegerField() 
    student_course = models.CharField(max_length = 100, null = False)

