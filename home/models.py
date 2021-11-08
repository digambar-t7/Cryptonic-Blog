from django.db import models

# Create your models here.
class Contact(models.Model):
    contactId = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(default=0)
    address = models.CharField(max_length=200)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    pin = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    