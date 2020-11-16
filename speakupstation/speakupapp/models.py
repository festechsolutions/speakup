from django.db import models, connections
from django.contrib.auth.models import User
# Create your models here.


class homePage1(models.Model):
    # currentQuantity = models.IntegerField()
    title = models.CharField(max_length=400)

    class Meta:
        db_table = "course"
        managed = False


class coursePage(models.Model):
    title = models.CharField(max_length=100)
    course_id = models.IntegerField()
    section_id = models.IntegerField()
    lesson_type = models.CharField(max_length=100)
    translator_sentence = models.CharField(max_length=500)
    translated_sentence = models.CharField(max_length=500)

    class Meta:
        db_table = "lesson"
        managed = False


class seperateId(models.Model):
    title = models.CharField(max_length=100)
    course_id = models.IntegerField()
    order = models.IntegerField()

    class Meta:
        db_table = "section"
        managed = False


class lesson1(models.Model):
    title = models.CharField(max_length=100)
    section_id = models.IntegerField()
    translator_sentence = models.CharField(max_length=100)
    translated_sentence = models.CharField(max_length=100)

    class Meta:
        db_table = "lesson"
        managed = False


class category1(models.Model):
    name = models.CharField(max_length=100)
    parent = models.IntegerField()

    class Meta:
        db_table = "category"
        managed = "False"
