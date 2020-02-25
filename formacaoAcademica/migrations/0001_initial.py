# Generated by Django 3.0.2 on 2020-02-25 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('pessoa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormacaoAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instituicao', models.CharField(max_length=100, verbose_name='Instituição')),
                ('inicio', models.DateField(verbose_name='Início')),
                ('fim', models.DateField(blank=True, null=True, verbose_name='Fim')),
                ('descricao', models.TextField(max_length=500, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('curso', models.CharField(max_length=100, verbose_name='Curso')),
                ('pessoa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='pessoa.Pessoa')),
            ],
        ),
    ]
