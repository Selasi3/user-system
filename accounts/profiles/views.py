from django.contrib.auth import login
from django.shortcuts import redirect, render
from django.urls import reverse
from profiles.forms import CustomUserCreationForm
from .forms import FileForm
from django.contrib.auth.decorators import login_required
from .models import FileUpload

def dashboard(request):
    return render(request, "profiles/dashboard.html")

def register(request):
    if request.method == "GET":
        return render(request, "profiles/register.html",
            {"form": CustomUserCreationForm})

    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

# @login_required
def entry(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        
        if form.is_valid():            
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect(reverse("dashboard"))

    else:
        form = FileForm()

    return render(request, "profiles/entry.html", {
        "form": form
    })

def uploaded_files(request,id):
    files = FileUpload.objects.get(pk=id)
    context = {
        "files":files

    }
    return render(request, "profiles/uploaded.html/", context)
