from django.urls import path
from . import views

urlpatterns = [
    path("addbook/", views.add_book, name="addbook"),
    path("addauthor/", views.add_author, name="addauthor"),
    path("updateauthor/", views.update_author, name="updateauthor"),
    path("addpublisher/", views.add_publisher, name="addpublisher"),
    path("updatepublisher/", views.update_publisher, name="updatepublisher"),
]
