from django.shortcuts import render, redirect
from .models import ItemAssigment
from .forms import ItemAssignmentForm
def home(request):
    if request.method == "POST":
        form = ItemAssignmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ItemAssignmentForm()

    return render(request, 'techboxapp/home.html', {'fm': form})

def base(request):
    return render(request, 'techboxapp/base.html')

