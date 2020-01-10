from django.db import models

class Visitor(models.Model):
    first_name = models.CharField(max_length=44)
    last_name = models.CharField(max_length=44)
    plate_number = models.CharField(max_length=8, unique=True, primary_key=True, default='0000-000')
    reason = models.TextField(max_length=100, null=True)
    present = models.BooleanField(default=True)
    arrival = models.DateTimeField(auto_now_add = True)
    departure = models.DateTimeField(auto_now=True)
    objects = models.Manager

    class Meta:
        db_table = 'Visitors'
        ordering = ['arrival']

    def __str__(self):
        return self.first_name +'\t'+ self.last_name