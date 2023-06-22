from rest_framework.views import APIView
from rest_framework import status
from .models import *
from .serializer import *
from rest_framework.response import Response
from rest_framework import generics

class AlunoAPIView(generics.ListCreateAPIView):

    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    # def get(self, request):
    #     alunos = Aluno.objects.all()
    #     serializer= AlunoSerializer(alunos, many=True)
    #     return Response(serializer.data)
    
    # def post(self, request):
    #     serializer = AlunoSerializer(data=request.data)
    #     if serializer.is_valid(raise_exception=True):
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
            

