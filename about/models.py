from django.db import models
from django.contrib.auth.models import User

# Create the about model
class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return  f"{self.title}"