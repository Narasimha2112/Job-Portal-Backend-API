from django.urls import path
from .views import JobListCreateView, JobRetrieveUpdateDeleteView

urlpatterns = [
    path("", JobListCreateView.as_view(), name="jobs"),
    path("<int:pk>/", JobRetrieveUpdateDeleteView.as_view(), name="job-detail"),
]
