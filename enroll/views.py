from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.
def add_show(request):
    if request.method == "POST":
        formObject = StudentRegistration(request.POST)
        if formObject.is_valid():
            nm = formObject.cleaned_data["name"]
            em = formObject.cleaned_data["email"]
            pw = formObject.cleaned_data["password"]
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            formObject = StudentRegistration()
    else:
        formObject = StudentRegistration()

    formfill = User.objects.all()
    return render(
        request, "enroll/addandshow.html", {"form": formObject, "formfill": formfill}
    )


# delete student
def delete_student(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()

        return HttpResponseRedirect("/")


# update student
def update_student(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        formObject = StudentRegistration(request.POST, instance=pi)
        if formObject.is_valid():
            formObject.save()
            formObject = StudentRegistration()
    else:
        pi = User.objects.get(pk=id)
        formObject = StudentRegistration(instance=pi)

    return render(request, "enroll/updatestudent.html", {"form": formObject})
