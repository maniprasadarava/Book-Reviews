from django.db import models

# Create your models here.
from django.db import models


class bookvendor(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    location = models.CharField(max_length=40)
    status = models.CharField(max_length=40, default="", editable=True)

    def __str__(self):
        return self.mail
    class Meta:
        db_table = 'bookvendor'


class upload(models.Model):
    filename = models.CharField(max_length=100)
    filetype = models.CharField(max_length=100)
    fileprice = models.CharField(max_length=100)
    #description = models.CharField(max_length=100,blank=True)
    file = models.FileField(upload_to='files/pdfs/')

    def __str__(self):
        return self.filename