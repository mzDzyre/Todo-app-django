from django.db import models

class Todo(models.Model):
    task = models.CharField(max_length=200, null=False)
    date = models.DateField()
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return self.task