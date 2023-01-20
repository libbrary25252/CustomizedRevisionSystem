from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.
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
    description  = models.TextField()
    def __str__(self):
        return self.description
