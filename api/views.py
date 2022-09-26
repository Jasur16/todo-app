from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from todo.models import TodoAppModel
from todo.serializers import TodoModelSerializers
from rest_framework import status


class MainView(APIView):

    def get(self, request):
        return Response({'ok': 'salom'})



class TodoView(APIView):

    def get(self, request):
            return Response(TodoModelSerializers(TodoAppModel.objects.filter(status=False), many=True).data)

    def post(self, request):
        serializers = TodoModelSerializers(data=request.data)

        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response({'error': 'Malumot kemadi'})

class DeleteView(APIView):
    def get_object(self, pk):
        try:
            return TodoAppModel.objects.get(pk=pk)
        except TodoAppModel.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        object = self.get_object(pk)
        object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class OzgarishView(APIView):
    def get_object(self, pk):
        try:
            return TodoAppModel.objects.get(pk=pk)
        except TodoAppModel.DoesNotExist:
            raise Response(status=status.HTTP_404_NOT_FOUND)

    def puch(self, request, pk):
        object = self.get_object(pk)
        serializers = TodoModelSerializers(object, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)
