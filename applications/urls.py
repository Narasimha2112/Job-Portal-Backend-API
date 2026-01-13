from django.urls import path
from .views import (
    ApplyJobView,
    MyApplicationsView,
    EmployerApplicationsView,
    UpdateApplicationStatusView,
)

urlpatterns = [
    path("apply/", ApplyJobView.as_view(), name="apply-job"),
    path("mine/", MyApplicationsView.as_view(), name="my-applications"),
    path("employer/", EmployerApplicationsView.as_view(), name="employer-applications"),
    path("<int:pk>/update-status/", UpdateApplicationStatusView.as_view(), name="update-status"),
]
