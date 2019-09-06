from rest_framework.response import Response
from .serializers import BoardSerializer, PlayerSerializer, MoveSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Board, Move, Player


class PlayerList(APIView):
    def get(self, request):
        list = Player.objects.all()[:2]
        data = PlayerSerializer(list, many=True).data
        return Response(data)

class PlayerApiUpdate(APIView):

    def put(self, request, id):
        position = get_object_or_404(Player, pk=id)
        if request.method == 'PUT':
            serializer = PlayerSerializer(position, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(PlayerSerializer(position).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BoardList(APIView):
    def get(self, request):
        list = Board.objects.all()[:3]
        data = BoardSerializer(list, many=True).data
        return Response(data)

class BoardDetail(APIView):
    def get(self, request, pk):
        detail = get_object_or_404(Board, pk=pk)
        data = BoardSerializer(detail).data
        return Response(data)

class MoveDetail(APIView):
    def get(self,request, pk):
        detail = get_object_or_404(Move, pk=pk)
        data = MoveSerializer(detail).data
        return Response(data)

class BoardApiUpdate(APIView):

    def put(self, request, id):
        position = get_object_or_404(Board, pk=id)
        if request.method == 'PUT':
            serializer = BoardSerializer(position, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(BoardSerializer(position).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
