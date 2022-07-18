
from rest_framework.response import Response		
from rest_framework.views import APIView		
from .models import Quiz
from rest_framework import permissions		
from .serializers import QuizSerializer
import random 



class randomQuiz(APIView):
    permission_classes=[permissions.AllowAny]		
    def get(self,request, id):		
        totalQuizs = Quiz.objects.all()
        randomQuizs=random.sample(list(totalQuizs), id)
        serializer = QuizSerializer(randomQuizs, many=True)
        return Response(serializer.data)






