from django.shortcuts import render,redirect
from portfolioapp.forms import UserForm
from portfolioapp.models import UserProfile

# Create your views here.
def index(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            print("Image upload Successfully")
            form.save()
            return redirect('Display')
    return render(request, 'index.html', {'form':form})

def display(request):
    data = UserProfile.objects.all()
    return render(request, 'Display.html', {'data':data})

def about(request):
    return render(request, 'About.html', {})

def profile(request):
    return render(request, 'Profile.html', {})
