# Generated by Django 2.1.2 on 2018-11-24 19:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_modalidade_limite'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicao',
            name='data_fim_incricoes',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='edicao',
            name='data_inicio_incricoes',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
