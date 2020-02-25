# Generated by Django 3.0.2 on 2020-02-25 04:28

from django.db import migrations, models
import pessoa.validador
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('sobreNome', models.CharField(max_length=100, verbose_name='Sobrenome')),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=12, verbose_name='Sexo')),
                ('dataNascimento', models.DateField(validators=[pessoa.validador.validarDataDeNascimento], verbose_name='data nascimento')),
                ('pais', models.CharField(max_length=100, verbose_name='País')),
                ('estado', models.CharField(max_length=100, verbose_name='Estado')),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('tempoExperiencia', models.CharField(max_length=100, verbose_name='Tempo experiência')),
                ('biografia', models.TextField(verbose_name='Sobre mim ')),
                ('foto', stdimage.models.StdImageField(upload_to='pessoa', verbose_name='Foto')),
            ],
        ),
    ]