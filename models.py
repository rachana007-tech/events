from django.db import models

class events(models.Model):
    event_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=20)
    desc=models.CharField(max_length=500)
    price=models.FloatField()
    limit=models.IntegerField()
class hosts(models.Model):
    host_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=60)
    place=models.CharField(max_length=40)
    image=models.TextField()

class eventshosts(models.Model):    
    event_host_id=models.AutoField(primary_key=True)
    event_id =models.ForeignKey(events,on_delete=models.CASCADE) 
    host_id=models.ForeignKey(hosts,on_delete=models.CASCADE) 

class registrations(models.Model):
    reg_id=models.AutoField(primary_key=True)
    email=models.EmailField()
    phone=models.CharField(max_length=12)
    event_id=models.ForeignKey(events,on_delete=models.CASCADE)    

