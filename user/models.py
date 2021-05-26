from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class userdata(models.Model):
    name = models.CharField(max_length=50)
    mail = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    qualification = models.CharField(max_length=40)
    status = models.CharField(max_length=40, default="", editable=True)

    def __str__(self):
        return self.mail

    class Meta:
        db_table = 'userdata'


class feedback(models.Model):
    bookname = models.CharField(max_length=100)
    booktype = models.CharField(max_length=100)
    bookprice = models.CharField(max_length=100)
    # file = models.FileField(upload_to='files/pdfs/')
    rating = models.CharField(max_length=200)
    review = models.CharField(max_length=200)


    def __str__(self):
        return self.bookname

    class Meta:
        db_table = 'userfeedback'