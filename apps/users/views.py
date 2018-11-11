from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """user register"""
    if request.method != 'POST':
        register_form = UserCreationForm()
    else:
        register_form = UserCreationForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            auth_user = authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            login(request, auth_user)
            return redirect('work_notes:index', permanent=True)

    context = {'register_form': register_form}
    return render(request, 'users/register.html', context)
