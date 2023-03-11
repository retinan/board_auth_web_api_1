from rest_framework import response, viewsets, permissions
from board.models import *
from api.serializers.boardSerializer import *


class BoardViewset(viewsets.ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer
    # permission_classes = ['AllowAny']

    def perform_create(self, serializer):
        serializer.save(user=User.objects.get(id=1))
