from django.db import models

#creamos modelo de estudiante
class cours(models.Model):
    idcourse= models.TextField(max_length=10)
    code    = models.TextField(max_length=8)
    name    = models.TextField()
    hour    = models.TextField()
    credits = models.TextField()
    state   = models.CharField(max_length=1)