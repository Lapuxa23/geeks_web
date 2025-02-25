from django.db import models
from django.contrib.auth.models import User

class CustomUser(User):
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    phone_number = models.CharField(max_length=14, default='+996')
    age = models.PositiveIntegerField(default=7)
    gender = models.CharField(max_length=1, choices=GENDER, default='M')
    experience = models.PositiveIntegerField(default=0)  # Для расчета ЗП
    salary = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.experience <= 1:
            self.salary = 1000
        elif 2 <= self.experience <= 3:
            self.salary = 2000
        elif 4 <= self.experience <= 5:
            self.salary = 3000
        else:
            self.salary = 5000
        super().save(*args, **kwargs)
