from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
from django.db.models import ForeignKey


class contributor(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, default=1)
    foss = models.CharField(max_length=200, default="")
    date1 = models.DateField(default=timezone.now)
    date2 = models.DateField(default=timezone.now)
    date3 = models.DateField(default=timezone.now)
    date4 = models.DateField(default=timezone.now)
    date5 = models.DateField(default=timezone.now)
    date6 = models.DateField(default=timezone.now)
    date7 = models.DateField(default=timezone.now)
    date8 = models.DateField(default=timezone.now)
    date9 = models.DateField(default=timezone.now)
    date10 = models.DateField(default=timezone.now)
    payment = models.IntegerField(default=0)

    def __str__(self):
        return self.foss