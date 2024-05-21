from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Student


def index(request):
    context = {'students': Student.objects.all()}
    return render(request, 'index.html', context)

def view_student(request, pk):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))