from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
import pdb

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        pdb.set_trace()
        if form.is_valid():
            # form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Account create for {username}!")
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'user/register.html', {'form': form})