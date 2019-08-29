from django.db import models

class Objects(models.Model):
    name_object = models.CharField(
        max_length=255,
    )
    name_work = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name_object

class Certificate(models.Model):
    page=models.ImageField(upload_to='certificates')

    def __unicode__(self):
        return  self.page.url


# Create your models here.
class Image(models.Model):
    img = models.ImageField(upload_to='images')

    def __unicode__(self):
        return self.img




class Contact(models.Model):
    name = models.CharField(max_length=30)
    subname = models.CharField(max_length=25)
    email = models.EmailField(max_length=25)

    phone = models.IntegerField()

    message = models.TextField(max_length=140)

