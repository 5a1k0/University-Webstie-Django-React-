from django.shortcuts import render
from rest_framework.generics import ListAPIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentDetailsSerializer, FacultyDetailsSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .models import StudentDetail, FacultyDetail
from .models import Notes
from .serializers import NotesSerializer

class NotesListView(APIView):
    def get(self, request, *args, **kwargs):
        notes = Notes.objects.all()  # Fetch all notes
        serializer = NotesSerializer(notes, many=True)  # Serialize them
        return Response(serializer.data)  # Return serialized data

class UserDetailsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # Check if user is part of the 'faculty' group
        if user.groups.filter(name='Faculty').exists():
            try:
                faculty_details = FacultyDetail.objects.get(user=user)
            except FacultyDetail.DoesNotExist:
                return Response({'detail': 'Faculty details not found.'}, status=404)

            serializer = FacultyDetailsSerializer(faculty_details)
            response_data = {
                'role': 'Faculty',
                'details': serializer.data
            }
            return Response(response_data)
        
        # Check if user is part of the 'student' group
        elif user.groups.filter(name='Students').exists():
            try:
                student_details = StudentDetail.objects.get(user=user)
            except StudentDetail.DoesNotExist:
                return Response({'detail': 'Student details not found.'}, status=404)

            serializer = StudentDetailsSerializer(student_details)
            response_data = {
                'role': 'Student',
                'details': serializer.data
            }
            return Response(response_data)
        
        # If user is neither in 'faculty' nor 'student' group
        else:
            return Response({'detail': 'User does not belong to faculty or student group.', 'role' : 'None'}, status=403)




# @api_view(['POST'])
# def login_view(request):
#     username = request.data.get('username')
#     password = request.data.get('password')

#     user = authenticate(request, username=username, password=password)
#     if user is not None:
#         refresh = RefreshToken.for_user(user)
#         return Response({
#             'refresh': str(refresh),
#             'access': str(refresh.access_token),
#         })
#     return Response({'error': 'Invalid credentials'}, status=400)




@api_view(['POST'])
def login_view(request):
    # Extract username and password from request data
    username = request.data.get('username')
    password = request.data.get('password')


    # Ensure username and password are provided
    if not username or not password:
        return Response({'error': 'Username and password are required'}, status=400)

    # Authenticate user using Django's built-in authentication
    user = authenticate(request, username=username, password=password)
    # If user is successfully authenticated
    if user is not None:
        print(user)
        # Check if user belongs to the 'student' or 'faculty' group
        is_student = StudentDetail.objects.filter(user=user).exists()
        is_faculty = FacultyDetail.objects.filter(user=user).exists()

        # Determine user type
        if is_student:
            user_type = 'student'
        elif is_faculty:
            user_type = 'faculty'
        else:
            return Response({'error': 'User not associated with student or faculty records'}, status=400)

        # Generate JWT tokens using SimpleJWT
        refresh = RefreshToken.for_user(user)

        # Return JWT tokens and user type
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'user_type': user_type,  # Return whether the user is a student or faculty
        })

    # If authentication fails (invalid credentials)
    return Response({'error': 'Invalid credentials'}, status=400)
