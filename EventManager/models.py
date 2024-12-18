from django.db import models


class Event(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 100)
    start_date = models.CharField(max_length = 50)
    end_date = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)


    def __str__(self):
        return self.name


