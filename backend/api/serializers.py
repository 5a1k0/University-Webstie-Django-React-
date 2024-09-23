from rest_framework import serializers
from .models import StudentDetail, FacultyDetail, Notes

class FacultyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyDetail
        fields = ['id', 'name', 'faculty_id', 'subject', 'user', 'number', 'short_name' ]# Include all fields you want to expose


class StudentDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentDetail
        fields = '__all__'

class NotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'title', 'pdf']  # Specify the fields to be included in the serialized output
