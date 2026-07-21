from django.db import models
from accounts.models import User
from applications.models import Application


class Document(models.Model):
    TYPE_TRANSCRIPT = 'transcript'
    TYPE_ID = 'national_id'
    TYPE_CERTIFICATE = 'certificate'
    TYPE_OTHER = 'other'
    TYPE_CHOICES = [
        (TYPE_TRANSCRIPT, 'Transcript'),
        (TYPE_ID, 'National ID'),
        (TYPE_CERTIFICATE, 'Certificate'),
        (TYPE_OTHER, 'Other'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    doc_type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    file = models.FileField(upload_to='documents/%Y/%m/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.email} - {self.doc_type}"
