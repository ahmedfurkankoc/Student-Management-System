from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student
from .forms import StudentForm


def index(request):
    context = {'students': Student.objects.all()}
    return render(request, 'index.html', context)

def view_student(request, pk):
    student = Student.objects.get(id=pk)
    return HttpResponseRedirect(reverse('index'))

def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_number = form.cleaned_data['student_number']
            new_first_number = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_gpa = form.cleaned_data['gpa']

            new_student = Student(
                student_number = new_student_number,
                first_name = new_first_number,
                last_name = new_last_name,
                email = new_email,
                field_of_study = new_field_of_study,
                gpa = new_gpa
            )
               
            new_student.save()

            context = {
                'form': StudentForm(),
                'success': True
                }
            
            return render(request, 'add.html', context)
    else:
        form = StudentForm()
    context = {'form': StudentForm()}
    return render(request, 'add.html', context)

def edit(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            context = {'form': form, 'success': True}
            return render(request, 'edit.html', context)
    else:
        student = Student.objects.get(id=pk)
        form = StudentForm(instance=student)

    context = {'form': form}
    return render(request, 'edit.html', context)

def delete(request, pk):
    if request.method == 'POST':
        student = Student.objects.get(id=pk)
        student.delete()
    return HttpResponseRedirect(reverse('index'))