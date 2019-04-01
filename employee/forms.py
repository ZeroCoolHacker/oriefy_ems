from django import forms
from employee.models import Employee

class BasicEmployeeCreateForm(forms.ModelForm):
    """
    Basic Information from an Employee
    """
    class Meta:
        model = Employee
        fields = [
        'picture',
        'temporary_address',
        'permanent_address',
        'linkdin_url',
        'facebook_url',
        'github_url',
        'father_name',
        'father_cnic',
        'fathers_phone_no'
    ]
