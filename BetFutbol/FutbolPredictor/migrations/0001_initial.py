# Generated by Django 3.0.3 on 2020-03-02 07:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='League',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='League name')),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200, verbose_name='Location')),
                ('date', models.DateTimeField(verbose_name='Match Date')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False, unique=True, verbose_name='Team name')),
                ('home_goals_scored', models.IntegerField()),
                ('away_goals_scored', models.IntegerField()),
                ('home_attacking_strength', models.FloatField()),
                ('away_attacking_strength', models.FloatField()),
                ('home_defensive_strength', models.FloatField()),
                ('away_defensive_strength', models.FloatField()),
                ('home_goal_conceded', models.IntegerField()),
                ('away_goal_conceded', models.IntegerField()),
                ('home_yellow_card_index', models.FloatField()),
                ('away_yellow_card_index', models.FloatField()),
                ('home_red_card_index', models.FloatField()),
                ('away_red_card_index', models.FloatField()),
                ('home_shot_on_target_index', models.FloatField()),
                ('away_shot_on_target_index', models.FloatField()),
                ('home_foul_index', models.FloatField()),
                ('away_foul_index', models.FloatField()),
                ('home_shot_index', models.FloatField()),
                ('away_shot_index', models.FloatField()),
                ('home_corner_kick_index', models.FloatField()),
                ('away_corner_kick_index', models.FloatField()),
                ('home_conversion_rate', models.FloatField()),
                ('away_conversion_rate', models.FloatField()),
                ('league', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FutbolPredictor.League')),
            ],
        ),
        migrations.CreateModel(
            name='Prediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winner', models.CharField(max_length=200, verbose_name='Predicted Winner')),
                ('confidence', models.FloatField(verbose_name='Win percentage')),
                ('predicted_date', models.DateTimeField(verbose_name='Prediction Date')),
                ('Match', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='FutbolPredictor.Match')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='away_team', to='FutbolPredictor.Team'),
        ),
        migrations.AddField(
            model_name='match',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='home_team', to='FutbolPredictor.Team'),
        ),
    ]
