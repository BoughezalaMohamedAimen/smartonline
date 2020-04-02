from .models import Chambre,Commande,Todo
from .serializers import ChambreSerializer,CommandeSerializer,CommandeListSerializer,TodoSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated








class ChambreListApi(APIView):
    """
    List all chambres, or create a new chambre.
    """


    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)


    def get(self, request, format=None):
        chambres = Chambre.objects.filter(user=request.user)
        serializer = ChambreSerializer(chambres, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ChambreSerializer(data=request.data)
        serializer.set_the_user(request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













class ChambreSingleSynchApi(APIView):

    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get_object(self, local,user):
        try:
            return Chambre.objects.get(user=user,local_id=local)
        except Chambre.DoesNotExist:
            raise Http404

    def get(self, request, local,format=None):
        chambres = self.get_object(local,request.user)
        serializer = ChambreSerializer(chambres, many=False)
        return Response(serializer.data)

    def put(self, request, local, format=None):
        chambre = self.get_object(local,request.user)
        if chambre.user==request.user:
            serializer = ChambreSerializer(chambre, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, local, format=None):
        chambre = self.get_object(local,request.user)
        if chambre.user==request.user:
            chambre.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)















class CommandeListApi(APIView):
    """
    List all chambres, or create a new chambre.
    """


    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)


    def get(self, request, format=None):
        commandes = Commande.objects.filter(user=request.user)
        serializer = CommandeListSerializer(commandes, many=True)
        return Response(serializer.data)



class CommandeAddApi(APIView):


    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get_chambre(self,local,user):
        try:
            return Chambre.objects.get(user=user,local_id=local)
        except Chambre.DoesNotExist:
            raise Http404

    def post(self, request,local_chambre, format=None):
        chambre=self.get_chambre(local_chambre,request.user)
        if chambre.user==request.user:
            serializer = CommandeSerializer(data=request.data)
            serializer.set_the_user_and_chambre(request.user,chambre)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)







class CommandeSingleSynchApi(APIView):

    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)



    def get_object(self, local,user):
        try:
            return Commande.objects.get(user=user,local_id=local)
        except Commande.DoesNotExist:
            raise Http404

    def get_chambre(self,local,user):
        try:
            return Chambre.objects.get(user=user,local_id=local)
        except Chambre.DoesNotExist:
            raise Http404



    def get(self, request, local_commande  ,format=None):
        commandes = self.get_object(local_commande,request.user)
        serializer = CommandeListSerializer(commandes, many=False)
        return Response(serializer.data)





    def put(self, request, local_commande, local_chambre=0,format=None):
        commande = self.get_object(local_commande,request.user)
        chambre = self.get_chambre(local_chambre,request.user)
        if commande.user==request.user:
            serializer = CommandeSerializer(commande, data=request.data)
            serializer.set_the_user_and_chambre(request.user,chambre)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, local_commande  , format=None):
        commande = self.get_object(local_commande,request.user)
        if commande.user==request.user:
            commande.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class TodoListApi(APIView):
    """
    List all chambres, or create a new chambre.
    """


    authentication_classes=(TokenAuthentication,)
    permission_classes=(IsAuthenticated,)

    def get_object(self, local,user):
        try:
            return Todo.objects.get(user=user,local_id=local)
        except Todo.DoesNotExist:
            raise Http404

    def get(self, request, id=0, format=None):
        todos = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    def post(self, request, id=0, format=None):
        serializer = TodoSerializer(data=request.data)
        serializer.set_the_user(request.user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id  , format=None):
        todo = self.get_object(id,request.user)
        if todo.user==request.user:
            todo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
