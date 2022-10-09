from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from .forms import PersonCreationForm, CreateUserForm
from .models import Person, City
from django.contrib.auth import authenticate, login, logout
from django.views.generic import ListView


def home(request):
    return render(request, 'index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('apply')
        else:
            messages.info(request, 'username or password is incorrect')

    return render(request, 'login.html')


def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    return render(request, 'register.html', {'form': form})


def logout_page(request):
    logout(request)
    return redirect('/')


def apply(request):
    return render(request, 'apply.html')


def person_create_view(request):
    form = PersonCreationForm()
    if request.method == 'POST':
        form = PersonCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'final.html',{'form':form})
    return render(request, 'home.html', {'form': form})


def person_update_view(request, pk):
    person = get_object_or_404(Person, pk=pk)
    form = PersonCreationForm(instance=person)
    if request.method == 'POST':
        form = PersonCreationForm(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    district_id = request.GET.get('district_id')
    cities = City.objects.filter(district_id=district_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
