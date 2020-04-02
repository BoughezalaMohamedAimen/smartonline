from rest_framework import serializers
from .models import Chambre,Commande,Todo
from django.http import Http404

class ChambreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chambre
        exclude =['user',]


    def set_the_user(self,user):
        self.user=user

    def create(self, validated_data):
        validated_data["user"] = self.user
        return super().create(validated_data)



class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        exclude =['user',]



    def set_the_user_and_chambre(self,user,chambre):
        self.user=user
        self.chambre=chambre

    def create(self, validated_data):
        validated_data["user"] = self.user
        validated_data["chambre"]=self.chambre
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["user"] = self.user
        validated_data["chambre"]=self.chambre

        return super().update(validated_data)


class CommandeListSerializer(serializers.ModelSerializer):
    chambre_local = serializers.SerializerMethodField('chambre_locall')
    class Meta:
        model = Commande
        exclude =['user',]


    def chambre_locall(self,instance):
      return instance.chambre.local_id


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        exclude =['user',]


    def set_the_user(self,user):
        self.user=user

    def create(self, validated_data):
        validated_data["user"] = self.user
        return super().create(validated_data)
