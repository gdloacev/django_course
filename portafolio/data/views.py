from django.shortcuts import render, redirect
from .forms import PersonForm
from .forms import ProjectForm
from .models import Person
from .models import Project

# Create your views here.
def person(request):
    person_form = PersonForm()

    if request.method == 'POST':
        person_form = PersonForm(request.POST, request.FILES)
        if person_form.is_valid():
            #person_form.save()
            newPerson = Person()
            newPerson.firstname = request.POST.get('firstname', '')
            newPerson.lastname = request.POST.get('lastname', '')
            newPerson.picture = person_form.cleaned_data['picture']
            newPerson.save()

            return redirect('/admin/')

    return render(request,'data/person.html',{'form':person_form})


def project(request):
    project_form = ProjectForm()

    projects = Project.objects.all()

    if request.method == 'POST':
        project_form = ProjectForm(request.POST, request.FILES)

        if project_form.is_valid():
            newProject = Project()
            newProject.image = project_form.cleaned_data['image']
            newProject.title = request.POST.get('title')
            newProject.description = request.POST.get('description')
            newProject.link = request.POST.get('link')
            newProject.save()   

            project_form = ProjectForm()         

    return render(request, 'data/projects.html',{'form':project_form, 'projects':projects})