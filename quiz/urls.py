from django.urls import path
from . import views

urlpatterns = [
    path("quiz/", views.get_quiz, name="get_quiz")
]