from django.urls import path
from . import views

urlpatterns = [
    path("quizzes/", views.list_quiz, name="get_quiz")
]
