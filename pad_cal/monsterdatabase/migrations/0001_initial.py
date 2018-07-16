# Generated by Django 2.0.7 on 2018-07-15 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActiveSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('skillID', models.IntegerField(blank=True, default=0)),
                ('skillType', models.IntegerField(blank=True, default=0)),
                ('levels', models.IntegerField(default=0)),
                ('maxTurns', models.IntegerField(blank=True, default=0)),
                ('minTurns', models.IntegerField(blank=True, default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Awakening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('effect', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CardNA',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activeSkill', models.ManyToManyField(to='monsterdatabase.ActiveSkill')),
            ],
        ),
        migrations.CreateModel(
            name='Evolution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evo', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='LeaderSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('skillID', models.IntegerField(blank=True, default=0)),
                ('skillType', models.IntegerField(blank=True, default=0)),
                ('doesNothing', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MonsterData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activeSkillID', models.IntegerField(blank=True, default=0)),
                ('ancestorID', models.IntegerField(default=0)),
                ('attributeID', models.IntegerField(default=0)),
                ('attribute', models.CharField(default='', max_length=100)),
                ('baseID', models.IntegerField(default=0)),
                ('cardID', models.IntegerField(default=0)),
                ('cost', models.IntegerField(default=0)),
                ('inheritable', models.BooleanField(default=False)),
                ('isCollab', models.BooleanField(default=False)),
                ('isReleased', models.BooleanField(default=False)),
                ('isUlt', models.BooleanField(default=False)),
                ('leaderSkillID', models.IntegerField(blank=True, default=0)),
                ('maxATK', models.IntegerField(default=0)),
                ('maxHP', models.IntegerField(default=0)),
                ('maxLevel', models.IntegerField(default=0)),
                ('maxRCV', models.IntegerField(default=0)),
                ('minATK', models.IntegerField(default=0)),
                ('minHP', models.IntegerField(default=0)),
                ('minRCV', models.IntegerField(default=0)),
                ('maxXP', models.IntegerField(default=0)),
                ('name', models.CharField(default='', max_length=200)),
                ('rarity', models.IntegerField(default=0)),
                ('subAttributeID', models.IntegerField(default=0)),
                ('subattribute', models.CharField(default='', max_length=100)),
                ('hp99', models.IntegerField(default=0)),
                ('atk99', models.IntegerField(default=0)),
                ('rcv99', models.IntegerField(default=0)),
                ('evomat1', models.IntegerField(default=0)),
                ('evomat2', models.IntegerField(default=0)),
                ('evomat3', models.IntegerField(default=0)),
                ('evomat4', models.IntegerField(default=0)),
                ('evomat5', models.IntegerField(default=0)),
                ('unevomat1', models.IntegerField(default=0)),
                ('unevomat2', models.IntegerField(default=0)),
                ('unevomat3', models.IntegerField(default=0)),
                ('unevomat4', models.IntegerField(default=0)),
                ('unevomat5', models.IntegerField(default=0)),
                ('type1', models.CharField(default='', max_length=100)),
                ('type2', models.CharField(default='', max_length=100)),
                ('type3', models.CharField(default='', max_length=100)),
                ('awakenings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monsterdatabase.Awakening')),
                ('evolutions', models.ManyToManyField(to='monsterdatabase.Evolution')),
            ],
        ),
        migrations.AddField(
            model_name='cardna',
            name='leaderSkill',
            field=models.ManyToManyField(to='monsterdatabase.LeaderSkill'),
        ),
        migrations.AddField(
            model_name='cardna',
            name='monster',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='monster', to='monsterdatabase.MonsterData'),
        ),
    ]
