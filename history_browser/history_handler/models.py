from django.db import models

class Host(models.Model):
    hostname = models.CharField(max_length=2048, primary_key=True)

class URL(models.Model):
    url = models.CharField(max_length=2048, primary_key=True)
    title = models.CharField(max_length=64, default='No Title')
    host_id = models.ForeignKey(Host, 
                                null=True,
                                on_delete=models.PROTECT) # TODO: fix name: host_id_id

class User(models.Model):
    username = models.CharField(max_length=2048)

class History(models.Model):
    url = models.ForeignKey(URL, models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
