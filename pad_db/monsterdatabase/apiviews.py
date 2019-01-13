from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Monster, Skill
from .serializers import MonsterSerializer, SkillSerializer


class MonsterList(APIView):
    def get(self, request):
        dungeons = Monster.objects.all()
        data = Monster.objects.values()
        return Response(data)




class SkillList(APIView):
    def get(self, request):
        dungeons = Skill.objects.all()
        data = Skill.objects.values()
        return Response(data)
