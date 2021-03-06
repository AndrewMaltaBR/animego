# Generated by Django 2.1.2 on 2018-11-24 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media')),
                ('nome_responsavel', models.CharField(max_length=120, null=True)),
                ('local', models.CharField(max_length=120, null=True)),
                ('data_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_fim', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Edicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(default=django.utils.timezone.now)),
                ('data_fim', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Estande',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('descricao', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media')),
                ('nome_responsavel', models.CharField(blank=True, max_length=120, null=True)),
                ('local', models.CharField(blank=True, max_length=120, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Edicao')),
            ],
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta', models.CharField(max_length=120)),
                ('reposta', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Foto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media')),
                ('descricao', models.TextField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Inscricao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Modalidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.FloatField()),
                ('atracoes', models.BooleanField()),
                ('palestras', models.BooleanField()),
                ('workshops', models.BooleanField()),
                ('torneios', models.BooleanField()),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Edicao')),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=60)),
                ('texto', models.TextField()),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media')),
                ('data_publicacao', models.DateTimeField(default=django.utils.timezone.now)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patrocinador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='media')),
                ('site', models.CharField(max_length=60)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Visitante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=60)),
                ('cpf', models.CharField(max_length=14)),
            ],
        ),
        migrations.AddField(
            model_name='inscricao',
            name='modalidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Modalidade'),
        ),
        migrations.AddField(
            model_name='inscricao',
            name='visitante',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Visitante'),
        ),
        migrations.AddField(
            model_name='atracao',
            name='edicao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Edicao'),
        ),
    ]
