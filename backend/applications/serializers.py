from rest_framework import serializers
from .models import Application


class ApplicationSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField(read_only=True)
    program_name = serializers.CharField(source='program.name', read_only=True)

    class Meta:
        model = Application
        fields = ('id', 'student', 'program', 'program_name', 'status', 'personal_statement', 'submitted_at', 'updated_at')
        read_only_fields = ('id', 'student', 'status', 'submitted_at', 'updated_at')


class ApplicationStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ('id', 'status')
