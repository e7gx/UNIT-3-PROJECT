# categories/models.py

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    parent_category = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE, related_name='subcategories')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
