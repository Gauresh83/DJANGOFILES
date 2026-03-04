from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

@login_required
def home(request):

    student_list = Student.objects.all()

    paginator = Paginator(student_list, 5)

    page_number = request.GET.get('page')

    students = paginator.get_page(page_number)

    return render(request,'home.html',{'students':students})
@login_required

def add_student(request):

    if request.method == "POST":

        form = StudentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('/')

    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
@login_required
def update_student(request,id):
    student = get_object_or_404(Student,id=id)
    form = StudentForm(request.POST or None,instance=student)

    if form.is_valid():
        form.save()
        return redirect('/')

    return render(request,'add_student.html',{'form':form})


@login_required
def delete_student(request,id):
    student = get_object_or_404(Student,id=id)
    student.delete()
    return redirect('/')