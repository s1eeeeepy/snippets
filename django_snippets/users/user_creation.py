# Custom user creation form

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    # set necessary data
    class Meta:
        model = User
        fields = [
            # fields
        ]
        labels = {
            {"old": "new"}
        }

# registration view

from .forms import CustomUserCreationForm
from django.shortcuts import redirect, render
from django.contrib import messages

# log in after registration

from django.contrib.auth import login

def registration(request):
    # can't reach page if user is logged in
    if request.user.is_authenticated:
        return redirect("URL_NAME")
    form = CustomUserCreationForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            # set username to lowercase
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            # log in user if necessary
            login(request, user)
            
            return redirect("URL_NAME")
        else:
            # send error message
    context = {"form": form}
    return render(request, "TEMPLATE_PATH"), context)
