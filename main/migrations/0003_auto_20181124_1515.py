# Generated by Django 2.1.2 on 2018-11-24 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20181124_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faq',
            name='admin',
        ),
        migrations.AlterField(
            model_name='patrocinador',
            name='site',
            field=models.URLField(blank=True, max_length=120, null=True),
        ),
        migrations.DeleteModel(
            name='Faq',
        ),
    ]
