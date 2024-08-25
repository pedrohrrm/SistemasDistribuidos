# Generated by Django 5.1 on 2024-08-24 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipe',
            name='formacao_academica',
            field=models.CharField(choices=[('M', 'Mestrado'), ('G', 'Graduação'), ('D', 'Doutorado')], default='G', max_length=30),
        ),
    ]
