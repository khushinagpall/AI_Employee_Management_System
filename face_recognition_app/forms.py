from django import forms
from .models import Employee  # Ensure you have an Employee model

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'position', 'department']  # Adjust these fields to match your model
