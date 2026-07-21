from rest_framework import serializers
from .models import Document


class DocumentSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Document
        fields = ('id', 'student', 'application', 'doc_type', 'file', 'uploaded_at')
        read_only_fields = ('id', 'student', 'uploaded_at')
