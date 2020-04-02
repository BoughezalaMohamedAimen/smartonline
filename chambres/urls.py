from django.contrib import admin
from django.urls import path,re_path
from .views import *
from .api import *

urlpatterns = [
        path('<int:id>', SingleChambre.as_view(),name='SingleChambre'),
        path('commande/<int:device>/<int:commande>',ChangeEtat.as_view(),name='ChangeEtat'),
        path('commande/<int:device>/',ChangeEtat.as_view(),name='ChangeEtat'),



        #------------------API ROUTES-----------------------------------#
        path('api', ChambreListApi.as_view(),name='ChambreListApi'),
        path('api/<int:local>', ChambreSingleSynchApi.as_view(),name='ChambreListApi'),

        path('commandes/api', CommandeListApi.as_view(),name='CommandeListApi'),
        path('commandes/api/add/<int:local_chambre>', CommandeAddApi.as_view(),name='CommandeAddApi'),
        path('commandes/api/<int:local_commande>', CommandeSingleSynchApi.as_view(),name='CommandeSingleApi'),
        path('commandes/api/<int:local_commande>/<int:local_chambre>', CommandeSingleSynchApi.as_view(),name='CommandeSingleApi'),

        path('todo/api/', TodoListApi.as_view(),name='TodoApi'),
        path('todo/api/<int:id>', TodoListApi.as_view(),name='TodoApi'),
]
