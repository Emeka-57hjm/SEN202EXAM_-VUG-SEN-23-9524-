from django.db import models

# Base class
class StaffBase(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_number= models.CharField(max_length=10)
    state = models.CharField(max_length=100)
   
    class Meta:
        abstract = True

    def get_role(self):
        return "Staff"

# Manager
class Manager(StaffBase):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    department = models.CharField(max_length=100)
    company_card = models.BooleanField(default=True)

    def get_role(self):
        return "Manager"

# Intern
class Intern(StaffBase):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mentor = models.ForeignKey(Manager, on_delete=models.CASCADE)
    phone_number= models.CharField(max_length=10)
    internship_end = models.DateField()
    

    def get_role(self):
        return "Intern"
    
class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
# Create your models here.
