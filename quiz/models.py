from django.db import models


# Create your models here.

class User(models.Model):
    USER_CATEGORIES = [
        ('ST', 'STUDENT'),
        ('TC', 'TEACHER'),
        ('FnF', 'FAMILY_AND_FRIENDS'),
        ('PR', 'PROFESSIONAL'),
    ]
    user_category = models.CharField(max_length=1, choices=USER_CATEGORIES, default='ST')
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.user_category


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='_("Category Name")')

    def __str__(self):
        return self.name


class Quiz(models.Model):
    USER_CATEGORIES = [
        ('ST', 'STUDENT'),
        ('TC', 'TEACHER'),
        ('FnF', 'FAMILY_AND_FRIENDS'),
        ('PR', 'PROFESSIONAL'),
    ]
    quiz_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='quizzes', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)
    questions = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    QUESTION_TYPES = [
        ('MC', 'Multiple Choice'),
        ('T/F', 'True or False'),
        ('ST', 'Short Text'),
    ]
    question_type = models.CharField(max_length=1, choices=QUESTION_TYPES, default='MC')
    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField(max_length=225)
    time_created = models.DateTimeField(auto_now_add=True)
    difficulty = models.IntegerField(choices=[
        (0, 'Easy'),
        (1, 'Medium'),
        (2, 'Hard')
    ], default=0)

    def __str__(self):
        return self.question_text


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_created = models.DateTimeField(auto_now_add=True)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.text


class Submission(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    answer_owner = models.ForeignKey(User, on_delete=models.CASCADE)
    time_submitted = models.DateTimeField(auto_now_add=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
