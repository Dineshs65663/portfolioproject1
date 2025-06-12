from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    userpic = models.ImageField(upload_to='userimg/', blank=True, null=True)
