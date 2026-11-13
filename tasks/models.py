from django.db import models

# Create your models here.

class Task(models.Model):
    
    title = models.CharField(max_length=200)

    description = models.TextField(blank=True)

    completed = models.BooleanField(default=False)
    
    
    priority = models.CharField(
        max_length=10,
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low'),
        ],
        default='Medium'
    )
    
    due_date = models.DateField(
        null=True,
        blank=True
    )


    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title