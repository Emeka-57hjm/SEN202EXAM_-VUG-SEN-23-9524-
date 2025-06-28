from django.contrib import admin
from .models import Manager, Intern, Address

admin.site.register(Address)
admin.site.register(Manager)
admin.site.register(Intern)


# Register your models here.
