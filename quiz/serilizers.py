from rest_framework import serializers

from quiz.models import Quiz


class QuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quiz
        fields = ['title', 'category', 'date_created']