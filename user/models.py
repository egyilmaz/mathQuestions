from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    # here I assume we will have 999 questions, with comma separation ,XXX
    # which makes 4 characters for each question, assuming 1000 questions, we need 4000 chars at max.
    questions = models.CharField(max_length=4000)


class Stats(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.IntegerField(default=1)
    presented = models.DateTimeField('date presented')
    actioned = models.DateTimeField('date actioned')
    event = models.CharField(max_length=10)  # skipped, success, failed
