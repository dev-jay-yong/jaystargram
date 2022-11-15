from django.db import models

# Create your models here.
class Feed(models.Model):
    user_id = models.IntegerField()
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_nick = models.TextField()
    like_count = models.IntegerField()
