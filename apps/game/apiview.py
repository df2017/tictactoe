from rest_framework.response import Response
from .serializers import BoardSerializer, PlayerSerializer, MoveSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Board, Move, Player


class PlayerList(APIView):
    def get(self, request):
        list = Player.objects.all()
        data = PlayerSerializer(list, many=True).data
        return Response(data)

    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PlayerApiUpdate(APIView):

    def get(self, request, id):
        detail = get_object_or_404(Player, pk=id)
        data = PlayerSerializer(detail).data
        return Response(data)

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
        list = Board.objects.all()
        data = BoardSerializer(list, many=True).data
        return Response(data)

    def post(self, request):
        serializer = BoardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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

class MoveList(APIView):
    def get(self, request):
        list = Move.objects.all()
        param = list.objects.get('position')
        data = MoveSerializer(param, many=True).data
        return Response(data)

class BoardApiUpdate(APIView):

    def put(self, request, id):
        position = get_object_or_404(Board, pk=id)
        serializer = BoardSerializer(position, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(BoardSerializer(position).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
