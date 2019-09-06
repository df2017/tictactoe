from rest_framework.response import Response
from .serializers import BoardSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Board


class BoardApi(APIView):

    def put(self, request, id):
        position = get_object_or_404(Board, pk=id)
        if request.method == 'PUT':
            serializer = BoardSerializer(position, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(BoardSerializer(position).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, id):
        params = get_object_or_404(Board, pk=id)
        if request.method == 'GET':
            serializer = BoardSerializer(params, data=request.data)
            if serializer.is_valid():
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
