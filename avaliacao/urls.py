from django.urls import path
from .views import *

urlpatterns = [
    path('alunos/', AlunoAPIView.as_view(), name='alunos')
]