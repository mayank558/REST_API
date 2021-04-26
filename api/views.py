from django.shortcuts import render
from django.http import Http404,JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import dataserializers
from base.models import task

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'get':'task-list/',
        'post':'task-edit/'
    }
    return Response(api_urls)

@api_view(['GET'])
def Tasklistview(request):
    allContent = task.objects.all()
    serializer = dataserializers(allContent, many=True)

    return Response(serializer.data)

@api_view(['POST'])
def TaskListedit(request):
    serializer=dataserializers(data=request.data)
    print(request.data);
    if serializer.is_valid():
        serializer.save()
    else:
        print("not a valid serializer")
    return Response(serializer.data)

