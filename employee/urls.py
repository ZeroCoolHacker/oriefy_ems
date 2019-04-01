from django.urls import path
from employee.views import EmployeeCreateView, EmployeeDetailView

app_name = 'employee'

urlpatterns = [
    path('profile/<int:pk>', EmployeeDetailView.as_view(), name='profile'),
    path('create', EmployeeCreateView.as_view(), name='create'),
]