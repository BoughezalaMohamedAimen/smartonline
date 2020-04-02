from django.contrib import admin
from .models import *



class ChambreAdmin(admin.ModelAdmin):
    list_display = ('id', 'nom')


admin.site.register(Chambre,ChambreAdmin)



class CommandeAdmin(admin.ModelAdmin):
    list_filter=['chambre','type']
    list_display = ('id','type','chambre', 'nom')





admin.site.register(Commande,CommandeAdmin)
