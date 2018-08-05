from django.shortcuts import render
from .models import Monster, Skill
from .maps import EXPLICIT_TYPE_MAP
import json


def cardView(request, card_id):
    template = 'monster_na.html'
    monster = Monster.objects.get(cardID=card_id)

    monsters = Monster.objects.all()

    # The following set of checks is necessary as some cards do not have leader skills, active skills, or ancestors.
    ancestor = None
    if monster.ancestorID != monster.cardID:
        if monster.ancestorID != 0:
            ancestor = Monster.objects.get(cardID=monster.ancestorID)

    activeskill = None
    leaderskill = None

    if Skill.objects.filter(skillID=monster.activeSkillID).first() is not None:
        activeskill = Skill.objects.get(skillID=monster.activeSkillID)
    if Skill.objects.filter(skillID=monster.leaderSkillID).first() is not None:
        leaderskill = Skill.objects.get(skillID=monster.leaderSkillID)

    multipliers = [1, 1, 1, 0]
    l_skills = []

    if leaderskill is not None:
        if leaderskill.c_skill_1 != -1:
            l_skills.append(Skill.objects.get(skillID=leaderskill.c_skill_1))
            l_skills.append(Skill.objects.get(skillID=leaderskill.c_skill_2))
            if leaderskill.c_skill_3 != -1:
                l_skills.append((Skill.objects.get(skillID=leaderskill.c_skill_3)))


        for skill in l_skills:

            multipliers[0] *= skill.hp_mult
            multipliers[1] *= skill.atk_mult
            multipliers[2] *= skill.rcv_mult
            if skill.dmg_reduction != 0:
                if multipliers[3] != 0:
                    multipliers[3] *= skill.dmg_reduction
                else:
                    multipliers[3] = skill.dmg_reduction
        multipliers[3] *= 100


    evos = None
    if len(monster.evolutions.all()) > 0:
        evos = []
        for evo in monster.evolutions.all():
            evoCard = Monster.objects.get(cardID=evo.evo)
            if "Alt." not in evoCard.name:
                evos.append(evoCard)

    evomats = getEvoMats(monster, monsters)
    unevomats = getUnEvoMats(monster, monsters)

    awakenings = json.loads(monster.awakenings)
    sawakenings = json.loads(monster.superAwakenings)

    types = getTypes(monster)

    context = {'activeskill': activeskill, 'leaderskill': leaderskill,
               'monster': monster, 'ancestor': ancestor, "evolutions": evos, "evomats": evomats,
               "unevomats": unevomats, 'awakenings': awakenings, 'sawakenings': sawakenings, 'types': types, 'lmultipliers': multipliers,}

    return render(request, template, context)


def cardList(request):
    rawCards = Monster.objects.order_by('cardID').all()
    cards = []
    cardID = []

    for card in rawCards:
        if "*" not in card.name:
            if "Alt." not in card.name:
                cards.append(card.name)
                cardID.append(card.cardID)

    cardList = zip(cards, cardID)
    context = {'cards': cardList}
    template = 'monster_list_na.html'
    return render(request, template, context)


def activeSkillListView(request):
    a_skills = Skill.objects.filter(skill_type="active")
    names = a_skills.values_list('name', flat=True)
    sids = a_skills.values_list('skillID', flat=True)
    skills = zip(names, sids)
    context = {'skills': skills}
    template = 'active_skill_list_na.html'
    return render(request, template, context)


def activeSkillView(request, id):
    skill = Skill.objects.get(skillID=id)
    monsters = Monster.objects.filter(activeSkillID=id)

    context = {'activeskill': skill, "monsters": monsters}
    template = 'active_skill_na.html'
    return render(request, template, context)


def leaderSkillListView(request):
    l_skills = Skill.objects.filter(skill_type="leader")
    names = l_skills.values_list('name', flat=True)
    sids = l_skills.values_list('skillID', flat=True)
    lSkills = zip(names, sids)
    context = {'skills': lSkills}
    template = 'leader_skill_list_na.html'
    return render(request, template, context)


def leaderSkillView(request, id):
    skill = Skill.objects.get(skillID=id)
    monsters = Monster.objects.filter(leaderSkillID=id)

    context = {'leaderskill': skill, "monsters": monsters}
    template = 'leader_skill_na.html'
    return render(request, template, context)


def getEvoMats(monster, monsters):
    evomats = []
    if monster.evomat1 != 0:
        evomats.append(monsters.get(cardID=monster.evomat1))
    if monster.evomat2 != 0:
        evomats.append(monsters.get(cardID=monster.evomat2))
    if monster.evomat3 != 0:
        evomats.append(monsters.get(cardID=monster.evomat3))
    if monster.evomat4 != 0:
        evomats.append(monsters.get(cardID=monster.evomat4))
    if monster.evomat5 != 0:
        evomats.append(monsters.get(cardID=monster.evomat5))
    return evomats


def getUnEvoMats(monster, monsters):
    evomats = []
    if monster.unevomat1 != 0:
        evomats.append(monsters.get(cardID=monster.unevomat1))
    if monster.unevomat2 != 0:
        evomats.append(monsters.get(cardID=monster.unevomat2))
    if monster.unevomat3 != 0:
        evomats.append(monsters.get(cardID=monster.unevomat3))
    if monster.unevomat4 != 0:
        evomats.append(monsters.get(cardID=monster.unevomat4))
    if monster.unevomat5 != 0:
        evomats.append(monsters.get(cardID=monster.unevomat5))
    return evomats


def getTypes(monster) -> []:
    types = []
    types.append(EXPLICIT_TYPE_MAP[int(monster.type1)])
    types.append(EXPLICIT_TYPE_MAP[int(monster.type2)])
    types.append(EXPLICIT_TYPE_MAP[int(monster.type3)])
    return types
