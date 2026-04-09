from django.shortcuts import render
from .models import Student

def index(request):
    if request.method == "POST":
        name = request.POST.get('name')
        marks = request.POST.get('marks')
        Student.objects.create(name=name, marks=marks)

    students = Student.objects.all()
    return render(request, 'index.html', {'students': students})
