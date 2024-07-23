from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloworld, name="helloworld"),
    path("time/<str:operator>/<int:hours>/", views.dynamicTime, name="dynamicTime"),
    path("variables", views.variables, name="variables"),
    path("tags/", views.tags, name="tags"),
    path("filters/", views.filters, name="filters"),
]
