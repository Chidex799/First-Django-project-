from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(unique=False, blank=False, null=False, max_length=50)
    pages_number = models.IntegerField(blank=True, null=True)
    publish_date = models.DateField(blank=False, null=False)
    author_name = models.CharField(blank=False, null=False, max_length=120)

    def __str__(self):
        return self.title
