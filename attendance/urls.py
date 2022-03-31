from django.urls import path
from . import views

urlpatterns = [
    path("mark_member/<int:id>",views.mark_member, name = "delete_attendance"),
    path("take_attendance",views.attendance, name = "attendance"),   
]