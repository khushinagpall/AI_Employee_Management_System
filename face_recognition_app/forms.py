from django import forms
from .models import Employee  # Ensure you have an Employee model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_id', 'name', 'email', 'photo', 'approval_status']  # Adjust these fields to match your model
