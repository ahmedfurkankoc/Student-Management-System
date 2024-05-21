from django.shortcuts import render
from .models import Student


def index(request):
    context = {'students': Student.objects.all()}
    return render(request, 'index.html', context)

