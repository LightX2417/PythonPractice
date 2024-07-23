from django.shortcuts import render
from django.http import HttpResponse
from .forms import SignUpForm

# Create a signup form using Django forms along with all the necessary validations.
def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            return HttpResponse(f"Hello, {first_name}! Form submitted successfully!")
    else:
        form = SignUpForm()

    return render(request, "formapp/signup.html", {"form": form})
