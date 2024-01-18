from django.db import models

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
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name + ' ' + self.last_name