from django.db import models
from django.conf import settings
from jobs.models import Job

# Create your models here.
class JobApplication(models.Model):
    class Status(models.TextChoices):
        SUBMITTED = "SUBMITTED", "Submitted"
        REVIEWED = "REVIEWED", "Reviewed"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"
    
    job = models.ForeignKey(
        Job,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    applicant = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="applications"
    )
    resume_link = models.TextField(blank=True)
    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.SUBMITTED
    )
    applied_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-applied_at"]
        unique_together = ("job", "applicant")
    
    def __str__(self):
        return f"{self.applicant.email} -> {self.job.title}"
    