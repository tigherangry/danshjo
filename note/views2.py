from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import notebock
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import Student2Serializer

@api_view(['GET', 'POST'])
def add(request):
    if request.method == 'GET':
        data = notebock.objects.all()
        serializer = Student2Serializer(data, many=True)
        return Response(serializer.data)
    else:
        serializer = Student2Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def shownote(request):
    data = notebock.objects.all()
    serializer = Student2Serializer(data, many=True)
    return Response(serializer.data)


@api_view([ "PUT"])
def noteupdate(request, student_id):
    try:
        student = notebock.objects.get(id=student_id)
        if request.method == 'PUT':
            serializer = Student2Serializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        return Response(Student2Serializer(student).data)
    except notebock.DoesNotExist:
        return Response(status=404)


@api_view([ 'DELETE'])
def deletenots(request, student_id):
    student = notebock.objects.get(id=student_id)
    serializer = Student2Serializer(student)
    try:
        student.delete()
        return Response(status=200)
    except:
        return Response(status=404)

@api_view(['GET'])
def getnote (request, student_id):
    try:
        student = notebock.objects.get(id=student_id)
        serializer = Student2Serializer(student)
    except:
        return Response(status=404)
    if request.method == "GET":
        return Response(serializer.data)


