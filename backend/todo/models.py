from django.db import models

# Create your models here.
class Todo(models.Model):
    titulo=models.CharField(max_length=150)
    descricao=models.CharField(max_length=500)
    completa=models.BooleanField(default=False)
    
    def __str__(self):
        return self.title