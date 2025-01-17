from django.urls import path

from . import views

app_name = "pdfs"
urlpatterns = [
    path("dashboard/", views.pdfs_dashboard, name="dashboard"),
    path("attendance/", views.attendance_report, name="attendance"),
    path("coursework/", views.coursework_report, name="coursework"),
    path("progress/", views.progress_report, name="progress"),
    path("resource/", views.resource_report, name="resource"),
]
