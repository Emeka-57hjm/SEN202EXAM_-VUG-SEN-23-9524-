from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Manager, Intern

class StaffRoleView(APIView):
    def get(self, request):
        data = []

        for manager in Manager.objects.all():
            data.append({
                'name': f"{manager.first_name} {manager.last_name}",
                'email': manager.email,
                'role': manager.get_role()
            })

        
        for intern in Intern.objects.all():
            data.append({
                'name': f"{intern.first_name} {intern.last_name}",
                'email': intern.email,
                'role': intern.get_role()
            })

        return Response(data)
# Create your views here.

