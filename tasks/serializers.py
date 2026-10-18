from rest_framework import serializers
from .models import Task

VALID_CATEGORIES = ['Personal', 'Work', 'Academic']


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'category', 'text', 'completed']

    def validate_category(self, value):
        if value not in VALID_CATEGORIES:
            raise serializers.ValidationError(
                f"category must be one of: {', '.join(VALID_CATEGORIES)}"
            )
        return value

    def validate_text(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("text cannot be empty.")
        return value
