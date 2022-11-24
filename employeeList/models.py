from django.db import models

# Create your models here.
class Employee(models.Model):

    GENDER =[
        ('M', "MALE"),
        ('F', "FEMALE"),
        ('o', "OTHERS"),
    ]
    DEPT_LIST = [
        ('T',"TECHNICAL"),
        ('N', "NON_TECHNICAL")
    ]
    POSITION_LIST = [
        ('CO', "COMPUTER_OPERATOR"),
        ('FS', "FULL_STACK_SENIOR"),
        ('FJ', "FULL_STACK_JUNIOR"),
        ('OT', "OTHERS"),
    ]
    STATUS_LIST = [
        ('A',"ACTIVE"),
        ('D', "DEACTIVe")
    ]

    eployee_id     = models.IntegerField()
    first_name     = models.CharField(max_length=60)
    last_name      = models.CharField(max_length=60)
    gender         = models.CharField( max_length=1, choices= GENDER, default='M')
    birthday       = models.DateField( auto_now=False, auto_now_add=False)
    email          = models.EmailField(max_length=254)
    contact        = models.IntegerField()
    department     = models.CharField( max_length=10, choices= DEPT_LIST)
    position       = models.CharField( max_length=10, choices= POSITION_LIST)
    date_hired     = models.DateField( auto_now=False, auto_now_add=False)
    monthly_salary = models.IntegerField()
    status         = models.CharField( max_length=10, choices= STATUS_LIST)