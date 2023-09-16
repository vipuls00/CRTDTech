from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
    field3 = models.BooleanField()
    field4 = models.DecimalField(max_digits=10, decimal_places=2)
    field5 = models.DateField()
    field6 = models.EmailField()
    field7 = models.URLField()
    field8 = models.FileField(upload_to='uploads/')

    # Add other fields as needed
