from django.shortcuts import render, redirect
from .forms import BookForm, AuthorForm, PublisherForm
from .models import Publisher, Author


def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addbook")
    else:
        form = BookForm()
    return render(request, "modelsapp/add_book.html", {"form": form})


def add_publisher(request):
    if request.method == "POST":
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "addpublisher"
            )  
    else:
        form = PublisherForm()
    return render(request, "modelsapp/add_publisher.html", {"form": form})


def update_publisher(request, pk):
    publisher = Publisher.objects.get(pk=pk)
    if request.method == "POST":
        form = PublisherForm(request.POST, instance=publisher)
        if form.is_valid():
            form.save()
            return redirect(
                "addpublisher"
            )  
    else:
        form = PublisherForm(instance=publisher)
    return render(request, "modelsapp/update_publisher.html", {"form": form})


def add_author(request):
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addauthor")  
    else:
        form = AuthorForm()
    return render(request, "modelsapp/add_author.html", {"form": form})


def update_author(request, pk):
    author = Author.objects.get(pk=pk)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect("addauthor")  
    else:
        form = AuthorForm(instance=author)
    return render(request, "modelsapp/update_author.html", {"form": form})
