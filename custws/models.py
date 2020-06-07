from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
import uuid


# Create your models here.

class UserData(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    SkypeId=models.CharField(max_length=100)
    PhoneNumber=models.IntegerField(blank=False)
    def __str__(self):
        return self.user.id

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=50)
    dateOfBirth=models.DateTimeField()
    MobileNo=models.IntegerField(max_length=20)
    houseNo=models.CharField(max_length=50)
    town=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pin=models.IntegerField(max_length=50)
    messenger=models.CharField(max_length=50)
    website=models.URLField(blank=True)



    def __str__(self):
        return f'{self.user.username} Profile'



class UserTaskDetails(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    TaskId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    custTaskId=models.IntegerField(default=0)
    taskName=models.TextField()
    taskDescription=models.TextField()
    taskCategory=models.CharField(max_length=100)
    taskSubCategory=models.CharField(max_length=100)
    taskAttachment1=models.URLField()
    taskAttachment2=models.URLField()
    taskRevenue=models.DecimalField(max_digits=10,decimal_places=2,default=100.00)
    taskStatus=models.CharField(max_length=100)
    creationTime=models.DateTimeField(default=now())
    lastUpdateTime=models.DateTimeField(auto_now=True)
    currency=models.CharField(max_length=100,default='NA')
    Sla=models.CharField(max_length=100,default='NA')
    paymentStatus=models.BooleanField(default=False)

    def __str__(self):
        return self.TaskId.hex

class TaskSolutions(models.Model):
    solutionId=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    task=models.ForeignKey(UserTaskDetails,on_delete=models.CASCADE)
    solutionDescription=models.TextField()
    solAttachment1=models.URLField()
    solAttachment2=models.URLField()
    creationTime=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.solutionId.hex



