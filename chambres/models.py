from django.contrib.auth.models import User
from django.db import models
import string
import secrets






class Chambre(models.Model):
    local_id=models.PositiveIntegerField(unique=True)
    nom=models.CharField(max_length=255)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank='true')

    class Meta:
        unique_together = ('local_id', 'user',)

    def __str__(self):
        return self.nom







class Commande(models.Model):
    class Type(models.TextChoices):
        lampe="Lampe"
        prise="Prise"
        rideau="Rideau"

    user=models.ForeignKey(User,on_delete=models.CASCADE,blank='true')
    chambre=models.ForeignKey(Chambre,on_delete=models.CASCADE,blank='true')
    local_id=models.PositiveIntegerField(unique=True)

    nom=models.CharField(max_length=255)
    type=models.CharField(max_length=255,choices=Type.choices)
    commande=models.CharField(max_length=255)
    commande2=models.CharField(max_length=255,blank=True,null=True)
    commande3=models.CharField(max_length=255,blank=True,null=True)
    etat=models.BooleanField(default=False)

    class Meta:
        unique_together = ('local_id', 'user',)



class Todo(models.Model):
    heure=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE,blank='true')
    local_id=models.PositiveIntegerField()
    commande=models.PositiveIntegerField()
    off_all=models.BooleanField(default=False)
