# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines for those models you wish to give write DB access
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

#Database objects

class Object(models.Model):
    object_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    code = models.CharField(max_length=10, blank=True)
    class Meta:
        managed = False
        db_table = 'objects'
    def __unicode__(self):  
        return self.name

class Type(models.Model):
    type_id = models.AutoField(primary_key=True)
    object = models.ForeignKey(Object)
    show_name = models.CharField(max_length=50, blank=True)
    name = models.CharField(max_length=50, blank=True)
    class Meta:
        managed = False
        db_table = 'types'
    def __unicode__(self):  
        return self.name

class UsersGroup(models.Model):
    user_group_id = models.AutoField(primary_key=True)
    group_type = models.ForeignKey(Type)
    user =  models.ForeignKey(User)
    class Meta:
        managed = False
        db_table = 'users_groups'
    def __unicode__(self):        
        user = User.objects.filter(id=self.user_id).values('username')[:1][0].get('username', None)
        group = Type.objects.filter(type_id = self.group_type_id).values('name')[:1][0].get('name', None)
        return  "%s - %s" % (user, group)

class City(models.Model):
    city_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, blank=True)
    latitude_degree = models.FloatField()
    longitude_degree = models.FloatField()
    class Meta:
        managed = False
        db_table = 'cities'
    def __unicode__(self):
        return self.name

class Venue(models.Model):
    venue_id = models.AutoField(primary_key=True)
    city = models.ForeignKey(City)
    sport_type = models.ForeignKey(Type, related_name='%(class)s_types_sport')
    group_type = models.ForeignKey(Type, related_name='%(class)s_types_group')
    name = models.CharField(max_length=50, blank=True)
    latitude_degree = models.FloatField()
    longitude_degree = models.FloatField()
    class Meta:
        managed = False
        db_table = 'venues'
    def __unicode__(self):  
        return self.name