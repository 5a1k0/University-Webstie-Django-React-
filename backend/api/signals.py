import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import StudentDetail, FacultyDetail

logger = logging.getLogger('api')

@receiver(post_save, sender=User)
def handle_user_save(sender, instance, created, **kwargs):
    if created:
        print(f"User created: {instance.username}")
        print(instance.groups.all())
        # Check and create FacultyDetails

        if instance.groups.filter(name='Faculty').exists():
            print(f"{instance.username} is in Faculty group.")
            faculty_detail, created = FacultyDetail.objects.get_or_create(user=instance)
            faculty_detail.save()
            if created:
                print(f"FacultyDetails created for {instance.username}.")
            else:
                print(f"FacultyDetails already exists for {instance.username}.")

        # Check and create StudentDetails
        if instance.groups.filter(name='Students').exists():
            print(f"{instance.username} is in Students group.")
            student_detail, created = StudentDetail.objects.get_or_create(user=instance)
            if created:
                print(f"StudentDetails created for {instance.username}.")
            else:
                print(f"StudentDetails already exists for {instance.username}.")
    else:
        if instance.groups.filter(name='Faculty').exists():
            faculty_detail, created = FacultyDetail.objects.get_or_create(user=instance)
            faculty_detail.save()
        if instance.groups.filter(name='Students').exists():
            student_detail, created = StudentDetail.objects.get_or_create(user=instance)
            student_detail.save()



# from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.dispatch import receiver
# from .models import StudentDetails

# @receiver(post_save, sender=User)
# def create_student_detail(sender, instance, created, **kwargs):
#     if created:
#         StudentDetails.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_student_detail(sender, instance, **kwargs):
#     instance.student_detail.save()