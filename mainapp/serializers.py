from rest_framework import serializers
from .models import Groups, Elements


class ElementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elements
        fields = ('name', 'parrent_group', 'created', 'moderated')


class GroupsSerializer(serializers.ModelSerializer):
    elements = ElementsSerializer(many=True, read_only=True)
    class Meta:
        model = Groups
        fields = ('parrent_group', 'name', 'description', 'image', 'elements')


