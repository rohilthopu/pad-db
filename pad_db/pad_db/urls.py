"""pad_cal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.conf import settings
from monsterdatabase import views as mv
from guerrilladungeon import views as gv
from dungeon import views as dv
from karmaleaderboard import views as kv

# API imports
from guerrilladungeon import apiviews as gav
from monsterdatabase import apiviews as mav
from karmaleaderboard import apiviews as kav
from dataversions import apiviews as dvav
from dungeon import apiviews as dav

from guerrilla import views as guerrilla_views
from monsters import views as monster_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    # Guerrilla Dungeons
    path('', gv.DungeonView),

    # NA Items
    path('monsterdb/na/', mv.cardList),
    path('monster/na/<int:card_id>/', mv.cardView),
    path('monster/na/edit/<int:card_id>/', mv.editCardView),
    path('dungeons/na/', dv.dungeonListView),
    path('dungeons/na/<int:d_id>/', dv.dungeonView),
    path('activeskills/na/', mv.activeSkillListView),
    path('activeskills/na/<int:skill_id>/', mv.activeSkillView),
    path('leaderskills/na', mv.leaderSkillListView),
    path('leaderskills/na/<int:skill_id>/', mv.leaderSkillView),
    path('leaderskills/na/edit/<int:skill_id>/', mv.editLeaderSkill),
    path('activeskills/na/edit/<int:skill_id>/', mv.editActiveSkill),

    path('leaderboard', kv.leaderboardView),

    # API views
    path('api/guerrilla/', gav.GuerrillaList.as_view()),
    path('api/monsters/na/', mav.MonsterList.as_view()),
    path('api/skills/na/', mav.SkillList.as_view()),
    path('api/leaderboard/', kav.LeaderboardList.as_view()),
    path('api/version/', dvav.VersionList.as_view()),
    path('api/dungeons/', dav.DungeonList.as_view()),
    path('api/floors/', dav.FloorList.as_view()),
    path('api/enemyskills/', mav.EnemySkillList.as_view()),
    path('api/encounters/', dav.EncounterList.as_view()),

    # new api endpoints
    path('api/guerrilla_dungeons/', guerrilla_views.guerrilla_view),
    path('api/monsters/', monster_views.monsters_view),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
