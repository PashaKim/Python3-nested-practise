from rest_framework import serializers
from .models import Groups, Elements


class ElementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elements
        fields = ('id', 'group', 'name', 'image', 'description', 'created')


class GroupsSerializer(serializers.ModelSerializer):
    subgroupselement = ElementsSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ('id', 'parent_group', 'name', 'description', 'image', 'subgroupselement',
                  'name_subgroup', 'count_subgroups', 'count_subelements')

