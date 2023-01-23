import uuid
import os
import datetime
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create models


class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    phone_no = PhoneNumberField(blank=True)
    create_date = models.DateField()
    role_id = models.ForeignKey(
        "Role", on_delete=models.CASCADE)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Role(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.description


class Question(models.Model):
    # def img_directory_path(instance, filename):
    #     ext = filename.split('.')[-1]
    #     filename = '{}.{}'.format(uuid.uuid4().hex[:10], ext)
    #     return os.path.join(instance.question_id, "img", filename)
    question_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    question_string = models.TextField()
    year = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=30)
    image = models.ImageField(
        upload_to="uploads/questions/", height_field=None, width_field=None, max_length=100, blank=True, null=True)
    options = models.JSONField("QuestionOptions", null=True, blank=True)
    answer = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.PROTECT)


class Category(models.Model):
    c_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    description = models.TextField()
