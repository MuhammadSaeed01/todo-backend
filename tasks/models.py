from django.db import models


class Task(models.Model):
    CATEGORY_CHOICES = [
        ('Personal', 'Personal'),
        ('Work', 'Work'),
        ('Academic', 'Academic'),
    ]

    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    text = models.CharField(max_length=500)
    completed = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f"[{self.category}] {self.text}"
