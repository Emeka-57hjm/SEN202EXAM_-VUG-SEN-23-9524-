from django.db import models


# Abstract base model
class StaffBase(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    class Meta:
        abstract = True

# Manager model
class Manager(StaffBase):
    department = models.CharField(max_length=100)
    company_card = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Manager"

# Intern model
class Intern(StaffBase):
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
    internship_end = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Intern"

# Create your models here.
