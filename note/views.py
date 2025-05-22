from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import danshjo
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StudentSerializer


@api_view(['GET', 'POST'])
def post(request):
    if request.method == 'GET':
        data = danshjo.objects.all()
        serializer = StudentSerializer(data, many=True)
        return Response(serializer.data)
    else:
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


@api_view(['GET'])
def show(request):
    data = danshjo.objects.all()
    serializer = StudentSerializer(data, many=True)
    return Response(serializer.data)


@api_view([ "PUT"])
def update(request, danshjo_id):
    try:
        student = danshjo.objects.get(id=danshjo_id)
        if request.method == 'PUT':
            serializer = StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=400)
        #return Response(StudentSerializer(student).data)
    except danshjo.DoesNotExist:
        return Response(status=404)


@api_view([ 'DELETE'])
def delete(request, student_id):
    student = danshjo.objects.get(id=student_id)
    serializer = StudentSerializer(student)
    try:
        student.delete()
        return Response(status=200)
    except:
        return Response(status=404)

@api_view(['GET'])
def get (request, student_id):
    try:
        student = danshjo.objects.get(id=student_id)
        serializer = StudentSerializer(student)
    except:
        return Response(status=404)
    if request.method == "GET":
        return Response(serializer.data)

