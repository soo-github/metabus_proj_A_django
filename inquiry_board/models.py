from django.conf import settings
from django.db import models

from accounts.models import User
from manageraccounts.models import ManagerAcc


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Inquiry(TimestampedModel):
    number = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    admin_id = models.ForeignKey(ManagerAcc, on_delete=models.CASCADE, blank=True)
    admin_answer = models.TextField(blank=True)