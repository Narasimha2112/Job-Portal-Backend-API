from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Job
from .serializers import JobSerializer
from accounts.permissions import IsEmployer

class JobListCreateView(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["created_at", "salary_range"]
    filterset_fields = ["location"]
    
    def perform_create(self, serializer):
        serializer.save(employer=self.request.user)
    
    def get_permissions(self):
        if self.request.method == "POST":
            return [IsEmployer()]
        return [permissions.AllowAny()]


class JobRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    def get_permissions(self):
        if self.request.method in ["PUT", "PATCH", "DELETE"]:
            return [IsEmployer()]
        return [permissions.AllowAny()]
    
    # Ensure only owner edits/deletes
    def perform_update(self, serializer):
        if self.request.user != self.get_object().employer:
            raise PermissionError("Not your job posting")
        serializer.save()
    
    def perform_destroy(self, instance):
        if self.request.user != instance.employer:
            raise PermissionError("Not your job posting")
        instance.delete()
