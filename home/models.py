from django.db import models
from django.db.models.deletion import CASCADE


class Users(models.Model):
    id = models.IntegerField(primary_key=True,)
    firstname= models.CharField(max_length=105)
    lastname= models.CharField(max_length=105)
    fullname= models.CharField(max_length=210)
    countryid= models.IntegerField()
    phonenumber= models.IntegerField()
    email= models.CharField(max_length=100)
    status = models.BooleanField(default=True)
    def __str_(self):
        return self.id
        
    
    
class Address(models.Model):
    userid = models.ForeignKey(Users,on_delete=models.CASCADE)
    address= models.CharField(max_length=500)
    city= models.CharField(max_length=500)
    state= models.CharField(max_length=500)
    postalcode= models.IntegerField()
    phoneprimary= models.IntegerField()
    phonesecondary= models.IntegerField()
    status = models.BooleanField(default=True)
    isdefault = models.BooleanField(db_column="isdef",default=True)
    def __str_(self):
        return self.userid