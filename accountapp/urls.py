		
from django.urls import path, include			
from .views import randomQuiz

urlpatterns = [path('v1/<int:id>/',randomQuiz.as_view()),]			