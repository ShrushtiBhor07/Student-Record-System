
from django.urls import path
from . import views
from .views import create_student

urlpatterns = [
    path('create/', create_student, name='create_student'),
    path('list/', views.list_students, name='list_students'),
    path('update/<int:pk>/',views.update_student,name='update_student'),
    path('delete/<int:pk>/', views.delete_student, name='delete_student'),
]
