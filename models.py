from django.db import models

# Create your models here.
class Ipadress(models.Model):
    ip = models.GenericIPAddressField(primary_key=True, protocol='both')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip

class Page(models.Model):
    ip = models.ForeignKey(
             'Ipadress',
              on_delete=models.CASCADE,)

    state = models.CharField(max_length=50)
    page = models.URLField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "ip : {} connected {}, date : {}".format(self.ip, self.page, self.created)

"""
class Post(models.Model):

class Get(models.Model):
"""
