from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Meeting, Meeting Minutes, Resource, Event

class Meeting(models.Model):
    meetingtitle=models.CharField(max_length=255)
    meetingdate=models.DateField()
    meetingtime=models.TimeField()
    location=models.TextField
    Agenda=models.URLField(null=True, blank=True)

    def __str__(self):
        return self.meetingtitile
    
    class Meta:
        db_table='meeting'

class MeetingMinutes(models.Model):
    meetingid=models.ForeignKey(Meeting, on_delete=models.DO_NOTHING)
    attendance=models.ManyToManyField(User)
    minutestext=models.TextField()

    def __str__(self):
        return self.meetingid
    
    class Meta:
        db_table='meetingminutes'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.TextField()
    url=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename
    
    class Meta:
        db_table='resource'

class Event(models.Model):
    eventtitle=models.CharField(max_length=255)
    location=models.TextField()
    date=models.DateField()
    time=models.TimeField()
    description=models.TextField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.eventtitle
    
    class Meta:
        db_table='event'