from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create the about model
class About(models.Model):
    """
    Stores a single about page
    """
    title = models.CharField(max_length=200, unique=True)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return  f"{self.title}"

class CollaborateRequest(models.Model):
    """
    Stores a single collaborate request message.
    """

    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"