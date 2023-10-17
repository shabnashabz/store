from datetime import datetime
from django.db import models
from datetime import date

# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     class meta:
#         db_table="User"

#     def __str__(self):
#         return self.username
# class register(models.Model):
#     username = models.CharField(max_length=100)
#     password = models.CharField(max_length=100)
#     cpassword = models.CharField(max_length=100)
#     class meta:
#         db_table="register"

#     def __str__(self):
#         return self.username

class Registration(models.Model):
   
    user_id= models.IntegerField(default=1)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dob = models.DateField(default='YYYY-MM-DD')
    age = models.IntegerField(default=18)
    gender= models.CharField(max_length=100,default='null')
    phn=models.IntegerField(default=1234567890)
    email=models.EmailField(default='null')
    add = models.CharField(max_length=255, default='null')
    depart= models.CharField(max_length=100,default='null')
    course= models.CharField(max_length=100,default='null')
    purpose= models.CharField(max_length=100,default='null')
    material= models.CharField(max_length=100,default='null')

    def __str__(self):
        return self.name

    
# class TABLE_payments (models.model):
 
#   order_id=models.IntegerField(),
#   payment_method= models.CharField(max_length=100),
#   amount=models.IntegerField(10,2),
#   created_at= models.DateTimeField(),
#   class meta:
#       db_table="TABLE_payments"
 