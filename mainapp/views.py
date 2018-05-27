from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from .models import Groups, Elements
from .serializers import GroupsSerializer, ElementsSerializer


# class GroupsListView(generics.ListAPIView):
#     queryset = Groups.objects.all().values()
#     serializer_class = GroupsSerializer
#
#
# class GroupsDetailView(generics.RetrieveAPIView):
#     queryset = Groups.objects.all().values()
#     serializer_class = GroupsSerializer


class GroupsViewSet(ModelViewSet):
    serializer_class = GroupsSerializer
    queryset = Groups.objects.all()

class ElementsViewSet(ModelViewSet):
    serializer_class = ElementsSerializer
    queryset = Elements.objects.all()

