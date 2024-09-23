from django.urls import path
from api import views
from .views import login_view, UserDetailsView, NotesListView
urlpatterns = [
    path('login/', login_view, name='login'),
    path('students-details/', UserDetailsView.as_view(), name='student-details'),
    path('notes/', NotesListView.as_view(), name='notes-list'),
]