from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentForm
from .models import Student  # ✅ Add this line

def create_student(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_student")  # Refresh page after submission
    return render(request, 'create_student.html', {'form': form})

def list_students(request):
    students = Student.objects.all()
    print("student count",students.count())
    for s in students:
        print(s.name,s.email,s.age)
    return render(request, 'list_students.html', {'students': students})

def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')  # make sure this matches your URL name
    else:
        form = StudentForm(instance=student)
    return render(request, 'update_student.html', {'form': form})

def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect('list_students')
