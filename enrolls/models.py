from collections.abc import Iterable
from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
    TITLE = (
        ('Mr', 'Mr'),
        ('Mrs', 'Mrs'),
        ('Miss', 'Miss'),
        ('Dr', 'Dr'),
        ('Prof', 'Prof'),
    )
    title = models.CharField(max_length=50, null=True, choices=TITLE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=18)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15,)
    department = models.CharField(max_length=50)
    doe = models.DateTimeField("employment_date", default=timezone.now)

    employee_id = models.CharField(max_length=10, unique=True, editable=False)

    def save(self, *args, **kwargs):
        if not self.employee_id:
            latest_employee = Employee.objects.order_by('-employee_id').first()
            if latest_employee:
                last_id = int(latest_employee.employee_id[3:])
                self.employee_id = 'EMP{:03d}'.format(last_id + 1)
            else:
                self.employee_id = 'EMP001'

        super(Employee, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.employee_id} - {self.first_name} {self.last_name}"
    
class Users(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username