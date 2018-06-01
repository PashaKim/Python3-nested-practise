from rest_framework import serializers
from .models import Groups, Elements


class ElementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Elements
        fields = ('id','name_group', 'parrent_group', 'name', 'image', 'description', 'created')

class GroupsSerializer(serializers.ModelSerializer):
    subgroupselement = ElementsSerializer(many=True, read_only=True)

    class Meta:
        model = Groups
        fields = ('id', 'name_group', 'parrent_group',  'name', 'description', 'image', 'subgroupselement',
                  'name_subgroup', 'count_subgroups', 'count_subelements')

