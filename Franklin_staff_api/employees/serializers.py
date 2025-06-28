from rest_framework import serializers
from .models import Manager, Intern

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['id', 'first_name', 'last_name', 'email', 'department', 'company_card']
        read_only_fields = ['company_card']  

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = ['id', 'first_name', 'last_name', 'email', 'mentor', 'internship_end']