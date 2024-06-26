from django.db import models
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    
    def _str_(self):
        return self.question_text
    objects = models.Manager()
    
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    
    def _str_(self):
        return self.option_text