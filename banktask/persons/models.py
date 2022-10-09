from django.db import models


class District(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class City(models.Model):
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Account(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name



class Person(models.Model):
    name = models.CharField(max_length=124)
    dob=models.DateTimeField(blank=True,null=True)
    age=models.IntegerField(blank=True,null=True)
    address=models.TextField(blank=True,null=True)
    contact=models.IntegerField(blank=True,null=True)
    email=models.EmailField(blank=True,null=True)
    creditcard=models.BooleanField(default=False)
    debitcard=models.BooleanField(default=False)
    chequebook=models.BooleanField(default=False)
    account=models.ForeignKey(Account,on_delete=models.SET_NULL, blank=True, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name