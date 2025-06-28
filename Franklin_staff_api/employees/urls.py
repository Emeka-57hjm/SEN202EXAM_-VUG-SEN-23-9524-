from django.urls import path
from .views import StaffRoleView

urlpatterns = [
    path('staff-roles/', StaffRoleView.as_view(), name='staff-roles'),
]
