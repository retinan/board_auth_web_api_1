from rest_framework import serializers
from board.models import *


class BoardSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.ReadOnlyField(source='user.email')
    class Meta:
        model = Board
        fields = ['title', 'content', 'user']
