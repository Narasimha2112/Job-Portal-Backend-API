from rest_framework import serializers
from .models import Job

class JobSerializer(serializers.ModelSerializer):
    employer_name = serializers.CharField(source="employer.name", read_only=True)
    employer_email = serializers.CharField(source="employer.email", read_only=True)
    
    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "description",
            "location",
            "salary_range",
            "created_at",
            "employer",
            "employer_name",
            "employer_email",
        ]
        read_only_fields = ["employer"]
