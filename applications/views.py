from rest_framework import generics, permissions
from .models import JobApplication
from .serializers import JobApplicationSerializer
from accounts.permissions import IsSeeker, IsEmployer

class ApplyJobView(generics.CreateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsSeeker]

    def perform_create(self, serializer):
        serializer.save(applicant=self.request.user)


# Seeker sees only own applications
class MyApplicationsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsSeeker]

    def get_queryset(self):
        return JobApplication.objects.filter(applicant=self.request.user)


# Employer sees applications for their jobs
class EmployerApplicationsView(generics.ListAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsEmployer]

    def get_queryset(self):
        return JobApplication.objects.filter(job__employer=self.request.user)


# Employer updates application status
class UpdateApplicationStatusView(generics.UpdateAPIView):
    serializer_class = JobApplicationSerializer
    permission_classes = [IsEmployer]
    queryset = JobApplication.objects.all()

    def perform_update(self, serializer):
        app = self.get_object()
        if app.job.employer != self.request.user:
            raise PermissionError("Not your candidate")
        serializer.save()
