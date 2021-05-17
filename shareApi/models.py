from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.

class UserProfile(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    boid_number = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Share(models.Model):
    name = models.CharField(max_length=250)
    shareId = models.IntegerField()
    created_date = models.DateTimeField(default=timezone.now, blank=True)
    updated_date = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return self.name

class ShareResult(models.Model):
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE, primary_key=True)
    share = models.ForeignKey(Share, on_delete=models.CASCADE)
    alloted_units = models.IntegerField(default=0)
    alloted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user.first_name + '-' + self.share.name + ('-alloted' if self.alloted else '-not alloted')
    

