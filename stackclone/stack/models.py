from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Questions(models.Model):
    description=models.CharField(max_length=200) 
    image=models.ImageField(upload_to="images",null=True,blank=True) 
    user=models.ForeignKey(User,on_delete=models.CASCADE) 
    created_date=models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self().description
    
    @property
    def question_answers(self):
        return Answers.objects.filter(question=self)

class Answers(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="auther")
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)
    created_date=models.DateField(auto_now_add=True)
    answer=models.CharField(max_length=200)
    up_vote=models.ManyToManyField(User,related_name="answer")
    
    @property
    def upvote_count(self):
        return self.up_vote.all().count()



