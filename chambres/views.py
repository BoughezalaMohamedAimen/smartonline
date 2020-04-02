from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Chambre,Commande
from django.http import HttpResponse
# from config.models import Config
import requests


# Create your views here.
class SingleChambre(TemplateView):
    def get(self,request,id):
        try:
            chambre=Chambre.objects.get(id=id)
            return render(request,'chambres/single.html',{'chambre':chambre})
        except:
            return redirect("Home")





class ChangeEtat(LoginRequiredMixin,TemplateView):
    def get(self,request,device,commande=1):
        try:
            print(request.user)
            # device=Commande.objects.get(id=device)
            # if request.user==device.user:
            #     if commande==1:
            #         print(device.commande)
            #         device.etat=not device.etat
            #         device.save()
            #     if commande==2:
            #         print(device.commande2)
            #     if commande==3:
            #         print(device.commande3)

            return HttpResponse(status=200)
        except:
            return HttpResponse(status=500)
