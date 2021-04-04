from django.conf import settings
from django.db import models
from django.utils import timezone

class Company(models.Model):
    PK_Company = models.AutoField(db_column='PK_Company', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description', blank=True, null=True)
    class Meta:
        db_table = 'Company'

    def __str__(self):
        return self.name

class Guide(models.Model):
    PK_Guide = models.AutoField(db_column='PK_Guide', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    phone = models.CharField(db_column='phone', max_length=11)
    PK_Company = models.ForeignKey(Company, models.DO_NOTHING, db_column='PK_Company')
    class Meta:
        db_table = 'Guide'

    def __str__(self):
        return self.name

class Place(models.Model):
    PK_Place = models.AutoField(db_column='PK_Place', primary_key=True)
    name = models.CharField(db_column='name', max_length=100)
    description = models.TextField(db_column='description', blank=True, null=True)
    imagepath = models.ImageField(db_column='imagePath', upload_to='photos', blank=True, null=True)
    class Meta:
        db_table = 'Place'

    def __str__(self):
        return self.name

class Excursion(models.Model):
    PK_Excursion = models.AutoField(db_column='PK_Excursion', primary_key=True)
    name = models.CharField(db_column='name_of_puzzle', max_length=200)
    description = models.TextField(db_column='description', blank=True, null=True)
    price = models.IntegerField(db_column='price')
    imagepath = models.ImageField(db_column='imagePath', upload_to='photos', blank=True, null=True)
    
    PK_Place = models.ForeignKey(Place, models.DO_NOTHING, db_column='PK_Place')
    PK_Guide = models.ForeignKey(Guide, models.DO_NOTHING, db_column='PK_Guide')

    def get_url(self):
        return reverse('excursioninfo',args=[str(self.PK_Excursion)])

    class Meta:
        db_table = 'Excursion'
class Schedule(models.Model):
    PK_Schedule = models.AutoField(db_column='PK_Schedule', primary_key=True)
    datetime = models.DateTimeField(db_column='datetime',blank=True, null=True)
    PK_Excursion = models.ForeignKey(Excursion, models.DO_NOTHING, db_column='PK_Excursion')
    class Meta:
        db_table = 'Schedule'
