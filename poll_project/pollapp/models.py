from django.db import models
class PollModel(models.Model):
   question=models.TextField()
   op1=models.CharField(max_length=100)
   op2=models.CharField(max_length=100)
   op3=models.CharField(max_length=100)
   op1c=models.IntegerField(default=0)
   op2c=models.IntegerField(default=0)
   op3c=models.IntegerField(default=0)
   def __str__(self):
       return self.question
   
