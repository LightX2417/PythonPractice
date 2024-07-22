from django.urls import path
from . import views

urlpatterns = [
    path("", views.helloworld, name="helloworld"),
    path("time/<str:operator>/<int:hours>/", views.dynamicTime, name="dynamicTime"),
]
