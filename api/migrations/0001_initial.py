# Generated by Django 4.1.2 on 2022-10-14 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fixture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_team', models.CharField(max_length=200)),
                ('home_squad', models.JSONField(null=True)),
                ('away_team', models.CharField(max_length=200)),
                ('away_squad', models.JSONField(null=True)),
                ('stadium', models.CharField(blank=True, max_length=200, null=True)),
                ('results', models.CharField(blank=True, max_length=200, null=True)),
                ('score', models.CharField(blank=True, max_length=200, null=True)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
            ],
        ),
    ]