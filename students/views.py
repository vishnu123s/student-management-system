from django.shortcuts import render, redirect, get_object_or_404
from .models import Student

def add_student(request):

    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]
        course = request.POST["course"]

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )

    return render(request, "add_student.html")


def student_list(request):

    students = Student.objects.all()

    return render(
        request,
        'student_list.html',
        {'students': students}
    )
def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    student.delete()

    return redirect('/students/')

def update_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.age = request.POST["age"]
        student.course = request.POST["course"]

        student.save()

        return redirect('/students/')

    return render(
        request,
        "update_student.html",
        {"student": student}
    )