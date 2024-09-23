from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FacultyDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='faculty_detail')
    name = models.CharField(max_length=100)
    faculty_id = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    number = models.CharField(max_length=100, default='XXXXX XXXXX')
    short_name = models.CharField(max_length=100, default = 'XXX')
    

class StudentDetail(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_detail')
    name = models.CharField(max_length=100)
    enrollment_number = models.CharField(max_length=50)
    roll_number = models.CharField(max_length=20)

    python_t1 = models.FloatField(null=True, blank=True)
    python_t2 = models.FloatField(null=True, blank=True)
    python_t3 = models.FloatField(null=True, blank=True)
    python_t4 = models.FloatField(null=True, blank=True)

    full_stack_development_t1 = models.FloatField(null=True, blank=True)
    full_stack_development_t2 = models.FloatField(null=True, blank=True)
    full_stack_development_t3 = models.FloatField(null=True, blank=True)
    full_stack_development_t4 = models.FloatField(null=True, blank=True)

    discrete_mathematics_t1 = models.FloatField(null=True, blank=True)
    discrete_mathematics_t2 = models.FloatField(null=True, blank=True)
    discrete_mathematics_t3 = models.FloatField(null=True, blank=True)
    discrete_mathematics_t4 = models.FloatField(null=True, blank=True)

    theory_of_computation_t1 = models.FloatField(null=True, blank=True)
    theory_of_computation_t2 = models.FloatField(null=True, blank=True)
    theory_of_computation_t3 = models.FloatField(null=True, blank=True)
    theory_of_computation_t4 = models.FloatField(null=True, blank=True)

    computer_organization_and_architecture_t1 = models.FloatField(null=True, blank=True)
    computer_organization_and_architecture_t2 = models.FloatField(null=True, blank=True)
    computer_organization_and_architecture_t3 = models.FloatField(null=True, blank=True)
    computer_organization_and_architecture_t4 = models.FloatField(null=True, blank=True)

    attendance = models.FloatField(null=True, blank=True)

class Notes(models.Model):
    title = models.CharField(max_length=255)
    pdf = models.FileField(upload_to='notes_pdfs/')

    def __str__(self):
        return self.title